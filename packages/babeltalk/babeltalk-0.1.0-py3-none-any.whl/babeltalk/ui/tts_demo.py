import gradio as gr
from babeltalk.tts import TTS


if __name__ == "__main__":
    tts = TTS()
    def generate_speech(text):
        return tts.generate_speech(text)
    
    demo = gr.Interface(
        fn=generate_speech,
        inputs=gr.Textbox(),
        outputs=gr.Audio(),
    )
    
    demo.launch(server_name="0.0.0.0")