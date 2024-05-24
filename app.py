"""
This module run an interface to edit a specific image
"""
import gradio as gr
import torch
from PIL import Image

from invertor.pte import PivotalTuningEdition

# You can change the path to your custom model
model = PivotalTuningEdition.load("./pte.pkl")

def generate(alpha_lips: float, alpha_hair: float, alpha_wrinkle: float) -> Image:
    """
    Generate the image

    :param alpha: Strength of editing
    :type alpha: float
    :return: Edited image
    :rtype: Image
    """
    return model.edit_pivot(torch.Tensor([alpha_lips, alpha_hair, alpha_wrinkle]).cuda())


with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            feature_lips = gr.Slider(minimum=-2, maximum=2, value=0, step=0.1, label="Lips")
            feature_hair = gr.Slider(minimum=-2, maximum=2, value=0, step=0.1, label="Hair")
            feature_wrinkle = gr.Slider(minimum=-2, maximum=2, value=0, step=0.1, label="Lion Wrinkle")
            btn = gr.Button("Run")

        output = gr.Image(type="pil")
        btn.click(fn=generate, inputs=[feature_lips, feature_hair, feature_wrinkle], outputs=output) # pylint: disable=E1101

demo.launch() # share=True, auth=("username", "JzshWD`=@.}nA&VaQ>^*B;HU-Ttm7LSj8xR_#M2+p$r:?wYdF~")
