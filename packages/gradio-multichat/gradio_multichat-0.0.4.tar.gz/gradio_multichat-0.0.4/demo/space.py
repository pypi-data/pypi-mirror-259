
import gradio as gr
from app import demo as app
import os

_docs = {'MultiChat': {'description': 'Creates a chatbot that displays user-submitted messages and responses. Supports a subset of Markdown including bold, italics, code, tables.\nAlso supports audio/video/image files, which are displayed in the MultiChat, and other kinds of files which are displayed as links. This\ncomponent is usually used as an output component.\n', 'members': {'__init__': {'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'height': {'type': 'int | str | None', 'default': 'None', 'description': 'The height of the component, specified in pixels if a number is passed, or in CSS units if a string is passed.'}, 'latex_delimiters': {'type': 'list[dict[str, str | bool]] | None', 'default': 'None', 'description': 'A list of dicts of the form {"left": open delimiter (str), "right": close delimiter (str), "display": whether to display in newline (bool)} that will be used to render LaTeX expressions. If not provided, `latex_delimiters` is set to `[{ "left": "$$", "right": "$$", "display": True }]`, so only expressions enclosed in $$ delimiters will be rendered as LaTeX, and in a new line. Pass in an empty list to disable LaTeX rendering. For more information, see the [KaTeX documentation](https://katex.org/docs/autorender.html).'}, 'rtl': {'type': 'bool', 'default': 'False', 'description': 'If True, sets the direction of the rendered text to right-to-left. Default is False, which renders text left-to-right.'}, 'show_share_button': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.'}, 'show_copy_button': {'type': 'bool', 'default': 'False', 'description': 'If True, will show a copy button for each chatbot message.'}, 'characters': {'type': 'dict | None', 'default': 'None', 'description': None}, 'sanitize_html': {'type': 'bool', 'default': 'True', 'description': 'If False, will disable HTML sanitization for chatbot messages. This is not recommended, as it can lead to security vulnerabilities.'}, 'render_markdown': {'type': 'bool', 'default': 'True', 'description': 'If False, will disable Markdown rendering for chatbot messages.'}, 'bubble_full_width': {'type': 'bool', 'default': 'True', 'description': 'If False, the chat bubble will fit to the content of the message. If True (default), the chat bubble will be the full width of the component.'}, 'line_breaks': {'type': 'bool', 'default': 'True', 'description': 'If True (default), will enable Github-flavored Markdown line breaks in chatbot messages. If False, single new lines will be ignored. Only applies if `render_markdown` is True.'}, 'likeable': {'type': 'bool', 'default': 'False', 'description': 'Whether the chat messages display a like or dislike button. Set automatically by the .like method but has to be present in the signature for it to show up in the config.'}, 'layout': {'type': '"panel" | "bubble" | None', 'default': 'None', 'description': 'If "panel", will display the chatbot in a llm style layout. If "bubble", will display the chatbot with message bubbles, with the user and bot messages on alterating sides. Will default to "bubble".'}}, 'postprocess': {'value': {'type': 'list[tuple[str, typing.Any]] | list[list[typing.Any]] | None', 'description': 'Receives a list of either list or turple of a pair of a strings. The first string represents the entity, while the second string represents the content.'}}, 'preprocess': {'return': {'type': 'list[tuple[str, str | None]] | None', 'description': 'Passes the messages in the chatbot as a `list[list[str, str | None]]`. The inner list has 2 elements:'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the MultiChat changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the MultiChat. Uses event data gradio.SelectData to carry `value` referring to the label of the MultiChat, and `selected` to refer to state of the MultiChat. See EventData documentation on how to use this event data'}, 'like': {'type': None, 'default': None, 'description': 'This listener is triggered when the user likes/dislikes from within the MultiChat. This event has EventData of type gradio.LikeData that carries information, accessible through LikeData.index and LikeData.value. See EventData documentation on how to use this event data.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'MultiChat': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_multichat`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_multichat/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_multichat"></a>  
</div>

A variant of Gradio's Chatbot component that can handle multiple entities, which can be useful for role-playing and/or multi-agent tasks.
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_multichat
```

## Usage

```python
import gradio as gr
from gradio_multichat import MultiChat

AVATARS = [
    "https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg",
    "https://images.pexels.com/photos/350784/pexels-photo-350784.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/2085831/pexels-photo-2085831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
]


SAMPLE = \"\"\"Blackholes:

In 1924, Arthur Eddington showed that the singularity disappeared after a change of coordinates, although it took until 1933 for Georges Lemaître to realize that this meant the singularity at the Schwarzschild radius was a non-physical coordinate singularity.</blockquote>

Arthur Eddington did however comment on the possibility of a star with mass compressed to the Schwarzschild radius in a 1926 book, noting that Einstein's theory allows us to rule out overly large densities for visible stars like Betelgeuse because "a star of 250 million km radius could not possibly have so high a density as the Sun.

In 1958, David Finkelstein identified the Schwarzschild surface as an event horizon, "a perfect unidirectional membrane: causal influences can cross it in only one direction".\"\"\"


def example(value):
    samples = []
    samples.append(["user", value])
    yield samples, samples
    samples.append(["bot", value])
    yield samples, samples
    samples.append(["carl", value])
    yield samples, samples
    samples.append(["john", SAMPLE])
    yield samples, samples
    samples.append(["carl", SAMPLE])
    yield samples, samples


entities = {
    "user": {
        "role": "user",
        "avatar": AVATARS[0],
    },
    "bot": {
        "role": "bot",  # Without avatar
    },
    "john": {
        "role": "user",
        "avatar": AVATARS[1],
    },
    "carl": {
        "role": "bot",
        "avatar": AVATARS[2],
    },
}


with gr.Blocks() as demo:
    with gr.Tab("boobles"):
        chatbot_a = MultiChat(
            label="CustomChat",
            characters=entities,
            layout="bubble",
            height=600,
            likeable=True,
            show_copy_button=True,
        )
    with gr.Tab("panels"):
        chatbot_b = MultiChat(
            label="CustomChat",
            characters=entities,
            layout="panel",
            height=600,
            likeable=True,
            show_copy_button=True,
        )
    with gr.Row():
        with gr.Column(scale=999):
            text_input = gr.Textbox(
                interactive=True,
                placeholder="Add you prompt here",
                container=False,
                lines=4,
                max_lines=4,
            )
        with gr.Column(min_width=98):
            with gr.Group():
                send_button = gr.Button("Send", variant="primary")
                clear_button = gr.Button("Clear")

        gr.on(
            [send_button.click, text_input.submit],
            example,
            text_input,
            [chatbot_a, chatbot_b],
        )

if __name__ == "__main__":
    demo.launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `MultiChat`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["MultiChat"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["MultiChat"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes the messages in the chatbot as a `list[list[str, str | None]]`. The inner list has 2 elements:.
- **As output:** Should return, receives a list of either list or turple of a pair of a strings. The first string represents the entity, while the second string represents the content.

 ```python
def predict(
    value: list[tuple[str, str | None]] | None
) -> list[tuple[str, typing.Any]] | list[list[typing.Any]] | None:
    return value
```
""", elem_classes=["md-custom", "MultiChat-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          MultiChat: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
