
import gradio as gr
from gradio_multichat import MultiChat


example = MultiChat().example_inputs()

with gr.Blocks() as demo:
    with gr.Row():
        MultiChat(label="Blank"),  # blank component
        MultiChat(value=example, label="Populated"),  # populated component


if __name__ == "__main__":
    demo.launch()
