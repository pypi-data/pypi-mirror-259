import gradio as gr
from gradio_multichat import MultiChat

AVATARS = [
    "https://thumbs.dreamstime.com/b/smiling-old-man-having-coffee-portrait-looking-happy-33471677.jpg",
    "https://images.pexels.com/photos/350784/pexels-photo-350784.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/2085831/pexels-photo-2085831.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
]


SAMPLE = """Blackholes:

In 1924, Arthur Eddington showed that the singularity disappeared after a change of coordinates, although it took until 1933 for Georges Lemaître to realize that this meant the singularity at the Schwarzschild radius was a non-physical coordinate singularity.</blockquote>

Arthur Eddington did however comment on the possibility of a star with mass compressed to the Schwarzschild radius in a 1926 book, noting that Einstein's theory allows us to rule out overly large densities for visible stars like Betelgeuse because "a star of 250 million km radius could not possibly have so high a density as the Sun.

In 1958, David Finkelstein identified the Schwarzschild surface as an event horizon, "a perfect unidirectional membrane: causal influences can cross it in only one direction"."""


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
