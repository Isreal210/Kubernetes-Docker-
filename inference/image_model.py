import torch
from transformers import AutoImageProcessor, SiglipForImageClassification
from PIL import Image

class ImageDeepfakeModel:
    def __init__(self, model_name="prithivMLmods/deepfake-detector-model-v1"):
        self.processor = AutoImageProcessor.from_pretrained(model_name)
        self.model = SiglipForImageClassification.from_pretrained(model_name)
        self.model.eval()

    def predict(self, img_path: str):
        img = Image.open(img_path).convert("RGB")
        inputs = self.processor(images=img, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model(**inputs)
            logits = outputs.logits
            probs = torch.softmax(logits, dim=1).squeeze().tolist()
        
        id2label = {str(i): label for i, label in enumerate(self.model.config.id2label)}
        return { id2label[str(i)]: probs[i] for i in range(len(probs)) }

