import torch
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan

from datasets import load_dataset

class TTS:
    """
    TTS is used to make speech from text.
    """
    def __init__(self, device = "cpu"):
        self.device = device
        self.processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
        self.model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
        self.model = self.model.to(device)
        embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
        self.speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
        self.speaker_embeddings = self.speaker_embeddings.to(device)
        self.vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
        self.vocoder = self.vocoder.to(device)

    def generate_speech(self, text):
        inputs = self.processor(text=text, return_tensors="pt").to(self.device)
        speech = self.model.generate_speech(inputs["input_ids"], 
                                       self.speaker_embeddings, 
                                       vocoder=self.vocoder)
        return speech.cpu().numpy()