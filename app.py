import os
import platform
import time

# Turn off Gradio telemetry before the library is imported
os.environ.setdefault("GRADIO_ANALYTICS_ENABLED", "False")

import gradio as gr


def echo(message, history):
    # Stream the response one letter at a time, with a pause
    response = f"You said: {message}"
    for i in range(len(response)):
        time.sleep(0.03)
        yield response[: i + 1]


with gr.Blocks(title="Gradio") as demo:
    gr.Markdown("# Hello world")
    gr.Markdown(
        f"Gradio: {gr.__version__} | Python: {platform.python_version()}"
    )
    gr.ChatInterface(
        fn=echo,
        examples=["Hello, Gradio!"],
    )

if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    demo.launch(server_name="0.0.0.0", server_port=port)
