from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

class TextDeepfakeModel:
    def __init__(self, model_name="roberta-base-openai-detector"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
        self.model.eval()

    def predict(self, text: str):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        probs = torch.softmax(logits, dim=1).squeeze().tolist()
        id2label = {str(i): label for i, label in enumerate(self.model.config.id2label)}
        return { id2label[str(i)]: probs[i] for i in range(len(probs)) }

