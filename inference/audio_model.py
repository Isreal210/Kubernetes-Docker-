import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2ForSequenceClassification

class AudioDeepfakeModel:
    def __init__(self, model_name="MelodyMachine/Deepfake-audio-detection-V2"):
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForSequenceClassification.from_pretrained(model_name)
        self.model.eval()

    def predict(self, audio_path: str):
        waveform, sr = torchaudio.load(audio_path)
        inputs = self.processor(waveform.squeeze(), sampling_rate=sr, return_tensors="pt", padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1).squeeze().tolist()
        id2label = {str(i): label for i, label in enumerate(self.model.config.id2label)}
        return { id2label[str(i)]: probs[i] for i in range(len(probs)) }

