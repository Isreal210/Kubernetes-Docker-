import cv2
import torch
import torchvision.transforms as T
from torch import nn

from inference.image_model import ImageDeepfakeModel  

class VideoDeepfakeModel(nn.Module):
    def __init__(self, image_model: ImageDeepfakeModel, hidden_size=256):
        super().__init__()
        self.image_model = image_model
       
        self.lstm = nn.LSTM(input_size=512, hidden_size=hidden_size, batch_first=True)
        self.classifier = nn.Linear(hidden_size, 2)

    def forward(self, frames_tensor):
       
        batch, seq, C, H, W = frames_tensor.size()
       
        feats = []
        for i in range(seq):
            frame = frames_tensor[:, i, :, :, :]
           
            feat = self.image_model.model.backbone(frame) 
            feats.append(feat)
        feats = torch.stack(feats, dim=1) 
        outputs, (hn, cn) = self.lstm(feats)
        logits = self.classifier(hn[-1])
        return logits

# Preprocessing to extract frames
def extract_frames(video_path: str, target_frames=16):
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
            frame = T.ToPILImage()(frame)
            frame = T.Resize((224,224))(frame)
            frame = T.ToTensor()(frame)
            frames.append(frame)
        count += 1
    cap.release()
    if len(frames) < target_frames:
        # pad or repeat last frame
        while len(frames) < target_frames:
            frames.append(frames[-1])
    return torch.stack(frames).unsqueeze(0)  

