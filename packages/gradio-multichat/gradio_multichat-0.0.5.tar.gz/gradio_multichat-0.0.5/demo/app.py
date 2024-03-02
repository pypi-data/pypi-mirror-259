import gradio as gr
from gradio_multichat import MultiChat as mc

css = """.john-msg-template {
  color: #f22ff0;
  background: #332211;
  font-size: 20px;
}"""

# style must be a css style set on the css parameter of the gr.blocks, in this case both John and Gust has two set up to them. john-msg-template
characters = [
    { "role": "Carl", "origin": "user", "avatar": "https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg"},
    { "role": "John", "origin": "bot", "avatar": "https://images.pexels.com/photos/350784/pexels-photo-350784.jpeg", "style": "john-msg-template"},
    { "role": "Gust", "origin": "user"},
]

def print_like_dislike(x: gr.LikeData):
    print(x.index, x.value, x.liked)

def example(value):
    samples = []
    samples.append({"role": "Carl", "content": value})
    yield samples, samples
    samples.append({"role": "John", "content": value})
    yield samples, samples
    samples.append({"role": "Ana", "content": value}) 
    yield samples, samples

with gr.Blocks(css=css) as demo:
    with gr.Tab("Style: Bubble"):
        chatbot_a = mc(
            label="CustomChat",
            characters=characters,
            layout="bubble",
            height=600,
            likeable=True,
            show_copy_button=True,
        )
    with gr.Tab("Style: Panel"):
        chatbot_b = mc(
            label="CustomChat",
            characters=characters,
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
    chatbot_a.like(print_like_dislike, None, None)
    chatbot_b.like(print_like_dislike, None, None)

if __name__ == "__main__":
    demo.launch()