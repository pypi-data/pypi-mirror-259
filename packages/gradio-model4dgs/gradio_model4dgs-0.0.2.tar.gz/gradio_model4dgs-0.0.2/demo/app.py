import gradio as gr
from gradio_model4dgs import Model4DGS
import os

examples = [os.path.join(os.path.dirname(__file__), example) for example in Model4DGS().example_inputs()]

with gr.Blocks() as demo:
    with gr.Row():
        Model4DGS(value=examples, label="4D Model")

if __name__ == "__main__":
    demo.launch()