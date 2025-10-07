import cv2
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as T

from inference.image_model import ImageDeepfakeModel


class VideoDeepfakeModel:

    def __init__(self, image_model: ImageDeepfakeModel, device=None, hidden_size=256):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.image_model = image_model
        self.image_model.model.to(self.device)
        self.image_model.model.eval()

        self.lstm = nn.LSTM(input_size=512, hidden_size=hidden_size, batch_first=True)
        self.classifier = nn.Linear(hidden_size, 2)
        self.to(self.device)

        self.transform = T.Compose([
            T.ToPILImage(),
            T.Resize((224, 224)),
            T.ToTensor(),
        ])

    def to(self, device):
        self.lstm.to(device)
        self.classifier.to(device)

    def extract_frames(self, video_path, target_frames=16):
        """
        Extracts a fixed number of frames from a video.
        Pads or repeats if fewer than target_frames exist.
        """
        cap = cv2.VideoCapture(video_path)
        frames = []
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        step = max(1, total // target_frames)
        count = 0

        while len(frames) < target_frames:
            ret, frame = cap.read()
            if not ret:
                break
            if count % step == 0:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = self.transform(frame)
                frames.append(frame)
            count += 1

        cap.release()
        if len(frames) == 0:
            raise ValueError("No frames extracted from video.")
        while len(frames) < target_frames:
            frames.append(frames[-1])  

        return torch.stack(frames).unsqueeze(0).to(self.device)

    @torch.no_grad()
    def predict(self, video_path):
        """
        Runs inference on a video and returns verdict/confidence.
        """
        frames_tensor = self.extract_frames(video_path)

        feats = []
        for i in range(frames_tensor.size(1)):
            frame = frames_tensor[:, i, :, :, :]
            feat = self.image_model.extract_features(frame)
            feats.append(feat)
        feats = torch.stack(feats, dim=1)

        
        outputs, (hn, cn) = self.lstm(feats)
        logits = self.classifier(hn[-1])
        probs = F.softmax(logits, dim=1)
        pred = torch.argmax(probs, dim=1).item()
        confidence = probs[0, pred].item()

        verdict = "fake" if pred == 1 else "real"
        return {"verdict": verdict, "confidence": round(confidence, 3)}
