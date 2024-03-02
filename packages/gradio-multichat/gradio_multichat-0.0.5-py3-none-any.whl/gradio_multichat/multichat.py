"""gr.Chatbot() component."""

from __future__ import annotations

import inspect
from pathlib import Path
from typing import Any, Dict, List, Literal, Optional, Tuple, Union

from gradio_client import utils as client_utils
from gradio_client.documentation import document

from gradio import processing_utils, utils
from gradio.components.base import Component
from gradio.data_classes import FileData, GradioModel, GradioRootModel
from gradio.events import Events
from gradio.utils import get_upload_folder
from enum import Enum


class RoleEnum(str, Enum):
    bot = "bot"
    user = "user"


class FileMessage(GradioModel):
    file: FileData
    alt_text: Optional[str] = None


class Entity(GradioModel):
    name: str
    role: RoleEnum
    avatar: Optional[str] = None


class ChatbotData(GradioRootModel):
    root: List[Dict[Any, Any]]


class MultiChat(Component):
    """
    Creates a chatbot that displays user-submitted messages and responses. Supports a subset of Markdown including bold, italics, code, tables.
    Also supports audio/video/image files, which are displayed in the MultiChat, and other kinds of files which are displayed as links. This
    component is usually used as an output component.

    Demos: chatbot_simple, chatbot_multimodal
    Guides: creating-a-chatbot
    """

    EVENTS = [Events.change, Events.select, Events.like]
    data_model = ChatbotData

    def __init__(
        self,
        value: list[tuple[str] | list[str]] | None = None,
        *,
        characters: list[dict] | None = None,
        label: str | None = None,
        every: float | None = None,
        show_label: bool | None = None,
        container: bool = True,
        scale: int | None = None,
        min_width: int = 160,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        height: int | str | None = None,
        latex_delimiters: list[dict[str, str | bool]] | None = None,
        rtl: bool = False,
        show_share_button: bool | None = None,
        show_copy_button: bool = False,
        sanitize_html: bool = True,
        render_markdown: bool = True,
        bubble_full_width: bool = True,
        line_breaks: bool = True,
        likeable: bool = False,
        layout: Literal["panel", "bubble"] | None = None,
    ):
        """
        Parameters:
            value: Default value to show in chatbot. If callable, the function will be called whenever the app loads to set the initial value of the component. Example: ``[{"role":"User", "content":"Hi john"}, {"role":"John", "content":"Hi User!"}]``
            characters: Prepares characters/agents to be used during the conversation, can be configured to include avatars, personalized ccs and origin/position (user/bot). Format: ``["role": str, "origin": "user" | "bot", "avatar": "https//www.domain.com/image.png" | "path/to/image.jpeg" | None, "style": str | None]``. Example: ``[{"role":"User", "origin": "user", "avatar":"/path/or/url/to/carl.png", "elem_class": None}, {"role":"John", "origin": "bot", "avatar":"/path/or/url/to/John.png", "elem_class": None}]``. The role is the name of the character and is also case sensitive, it will not determine the postion of the chat, just its tag.  To determine where the message's positon for that character, we use `origin` variable, where it can be set to either "user" or "bot". If unset or set differently will raise an value error. The `style` should have the CSS style that was set on the block's css, it will change the content inside the response, either being the ballon or being the panel layout.
            label: The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.
            every: If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute.
            show_label: if True, will display label.
            container: If True, will place the component in a container - providing some extra padding around the border.
            scale: relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.
            min_width: minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            height: The height of the component, specified in pixels if a number is passed, or in CSS units if a string is passed.
            latex_delimiters: A list of dicts of the form {"left": open delimiter (str), "right": close delimiter (str), "display": whether to display in newline (bool)} that will be used to render LaTeX expressions. If not provided, `latex_delimiters` is set to `[{ "left": "$$", "right": "$$", "display": True }]`, so only expressions enclosed in $$ delimiters will be rendered as LaTeX, and in a new line. Pass in an empty list to disable LaTeX rendering. For more information, see the [KaTeX documentation](https://katex.org/docs/autorender.html).
            rtl: If True, sets the direction of the rendered text to right-to-left. Default is False, which renders text left-to-right.
            show_share_button: If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.
            show_copy_button: If True, will show a copy button for each chatbot message.
            sanitize_html: If False, will disable HTML sanitization for chatbot messages. This is not recommended, as it can lead to security vulnerabilities.
            render_markdown: If False, will disable Markdown rendering for chatbot messages.
            bubble_full_width: If False, the chat bubble will fit to the content of the message. If True (default), the chat bubble will be the full width of the component.
            line_breaks: If True (default), will enable Github-flavored Markdown line breaks in chatbot messages. If False, single new lines will be ignored. Only applies if `render_markdown` is True.
            likeable: Whether the chat messages display a like or dislike button. Set automatically by the .like method but has to be present in the signature for it to show up in the config.
            layout: If "panel", will display the chatbot in a llm style layout. If "bubble", will display the chatbot with message bubbles, with the user and bot messages on alterating sides. Will default to "bubble".
        """
        # self.GRADIO_CACHE = get_upload_folder
        self.likeable = likeable
        self.height = height
        self.rtl = rtl
        if latex_delimiters is None:
            latex_delimiters = [{"left": "$$", "right": "$$", "display": True}]
        self.latex_delimiters = latex_delimiters
        self.show_share_button = (
            (utils.get_space() is not None)
            if show_share_button is None
            else show_share_button
        )
        self.render_markdown = render_markdown
        self.show_copy_button = show_copy_button
        self.sanitize_html = sanitize_html
        self.bubble_full_width = bubble_full_width
        self.line_breaks = line_breaks
        self.layout = layout
        self.characters = {
            "user": {"origin": "user", "avatar": None, "style": None},
            "bot": {"origin": "bot", "avatar": None, "style": None},
        }
        self.new_characters = characters
        super().__init__(
            label=label,
            every=every,
            show_label=show_label,
            container=container,
            scale=scale,
            min_width=min_width,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            value=value,
        )
        if self.new_characters or not self.characters:
            self._setup_characters()

    def _setup_characters(self):
        if isinstance(self.new_characters, list):
            for content in self.new_characters:
                role = content.get("role")
                origin = content.get("origin")
                if not isinstance(role, str) or not role.strip():
                    raise ValueError(
                        f'The role is not a non-empty string. "role" = {role}'
                    )
                if not isinstance(origin, str) or origin not in ["user", "bot"]:
                    raise ValueError(
                        "The origin provided is not valid.",
                        f"It must be 'user' or 'bot'. \"origin\" = {origin}.",
                    )
                self.characters.update(
                    {
                        role: {
                            "origin": origin,
                            "avatar": processing_utils.move_resource_to_block_cache(
                                content.get("avatar"), self
                            ),
                            "style": content.get("style"),
                        }
                    }
                )
        self.new_characters = {}

    def _preprocess(
        self, contents: FileMessage | None
    ) -> Optional[Union[str | FileMessage]]:
        if isinstance(contents, FileMessage):
            if contents.alt_text:
                return (contents.file.path, contents.alt_text)
            else:
                return (contents.file.path, None)
        elif isinstance(contents, str):
            return contents
        else:
            return None
    def preprocess(
        self,
        payload: list[dict] | ChatbotData | None,
    ) -> List[Tuple[str, str | None]] | None:
        """
        Parameters:
            payload: data as a ChatbotData object
        Returns:
            A list of elements ready to deploy
        """
        if not isinstance(payload, list):
            return None
        processed_messages = []
        for message in payload:
            if not isinstance(message, dict):
                raise TypeError(f"Expected List[dict]. Received: {message}")

            role = message.get("role")
            content = message.get("content")
            if not isinstance(role, str) or not role.strip():
                raise ValueError(
                    "The role of the message must be set! It cannot be a non-string or an empty string."
                )
            char_data = self.characters.get(role, {"origin": "bot"})

            processed_messages.append(
                {
                    "role": role,
                    "message": self._preprocess(content),
                    "avatar": char_data.get("avatar"),
                    "origin": char_data.get("origin"),
                    "style": char_data.get("style"),
                }
            )
        return processed_messages

    def _postprocess_text(
        self, message: Optional[Union[str | tuple | list]]
    ) -> str | FileMessage | None:
        if not message:
            return None
        elif isinstance(message, (tuple, list)):
            filepath = str(message[0])

            mime_type = client_utils.get_mimetype(filepath)
            return FileMessage(
                file=FileData(path=filepath, mime_type=mime_type),
                alt_text=message[1] if len(message) > 1 else None,
            )
        elif isinstance(message, str):
            message = inspect.cleandoc(message)
            return message
        else:
            raise ValueError(f"Invalid message for MultiChat component: {message}")

    def _postprocess(self, char_name: str, char_content: str | None) -> dict:
        char_data = self.characters.get(char_name, {"origin": "bot"})
        return {
            "role": char_name,
            "message": self._postprocess_text(char_content),
            "avatar": char_data.get("avatar"),
            "origin": char_data.get("origin"),
            "style": char_data.get("style"),
        }

    def postprocess(
        self,
        value: Optional[List[Tuple[str, Any]] | List[List[Any]]],
    ) -> ChatbotData:
        """
        Parameters:
            value: Receives a list of either list or turple of a pair of a strings. The first string represents the entity, while the second string represents the content.
        Returns:
            An object of type ChatbotData
        """
        if value is None:
            return ChatbotData(root=[])

        # here for value initialization, if removed, will be problematic
        if not self.characters or self.new_characters:
            self._setup_characters()

        processed_messages = []
        for message in value:
            if not isinstance(message, dict):
                raise TypeError(
                    f"Expected a list with dictionaries. Received: {message}"
                )
            char_name = message.get("role")
            char_content = message.get("content")
            if not isinstance(char_name, str) or not char_name.strip():
                raise ValueError(
                    f"Invalid role '{char_name}'! It is required to be a non-empty string."
                )
            processed_messages.append(
                self._postprocess(char_name, char_content),
            )
        return ChatbotData(root=processed_messages)

    def example_inputs(self) -> Any:
        return [{"role":"user", "content":"Hi!"}, {"role":"bot", "content":"Hello there!"}]
