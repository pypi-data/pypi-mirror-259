
import gradio as gr
from gradio_multichat import MultiChat

def example(value):
    return "", [
        ["user", value],
        ["bot", f"World!"],
        ["john", "Hello, Get Up!"],
        ["carl", "..."],
    ]


entities = {
    "user": {
        "role": "user",
        "avatar": "https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg",
    },
    "bot": {
        "role": "bot",
        "avatar": "https://th.bing.com/th/id/OIP.sU-uj10S6p05niuTGnpkUgAAAA?rs=1&pid=ImgDetMain",
    },
    "john": {
        "role": "user",
        "avatar": "https://images.pexels.com/photos/350784/pexels-photo-350784.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    },
    "carl": {
        "role": "bot",
        "avatar": "https://images.pexels.com/photos/2085831/pexels-photo-2085831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    },
}


with gr.Blocks() as demo:
    with gr.Row():
        chatbot = MultiChat(
            value=[],
            label="CustomChat",
            characters=entities,
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
            [text_input, chatbot],
        )

if __name__ == "__main__":
    demo.launch()
