from gradio_client import Client
import gradio as gr

client = Client("stabilityai/stable-diffusion-3-medium")

def generate_image(prompt):
    result = client.predict(
        prompt=prompt,
        negative_prompt="",
        seed=0,
        randomize_seed=True,
        width=1024,
        height=1024,
        guidance_scale=5,
        num_inference_steps=28,
        api_name="/infer"
    )
    # Assuming the image is the first element of the tuple
    image = result[0]
    return image

interface = gr.Interface(fn=generate_image, inputs="text", outputs="image")
interface.launch()