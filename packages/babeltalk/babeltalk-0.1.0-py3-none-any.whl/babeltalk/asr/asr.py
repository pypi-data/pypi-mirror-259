from transformers import pipeline

class ASR:
    """
    ASR is used to transcribe text from a speech audio.
    """
    def __init__(self,
                 model_id = "openai/whisper-large-v3",
                 device = "cpu"):
        self.device = device
        self.pipe = pipeline("automatic-speech-recognition", 
                             model=model_id, device=device
                    )

    def transcribe_speech(self, filepath):
        output = self.pipe(
            filepath,
            max_new_tokens=256,
            generate_kwargs={
                "task": "transcribe"
            },
            chunk_length_s=30,
            batch_size=8,
        )
        return output["text"]