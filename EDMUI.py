from gradio_client import Client

client = Client("stabilityai/stable-diffusion-3-medium")
result = client.predict(
		prompt="starbuck promotion poster",
		negative_prompt="",
		seed=0,
		randomize_seed=True,
		width=1024,
		height=1024,
		guidance_scale=5,
		num_inference_steps=28,
		api_name="/infer"
)
print(result)

# import gradio as gr
# def generate_image(prompt):
#     result = client.predict(
#         prompt=prompt,
#         negative_prompt="",
#         seed=0,
#         randomize_seed=True,
#         width=1024,
#         height=1024,
#         guidance_scale=5,
#         num_inference_steps=28,
#         api_name="/infer"
#     )
#     return result

# interface = gr.Interface(fn=generate_image, inputs="text", outputs="image")
# interface.launch()
