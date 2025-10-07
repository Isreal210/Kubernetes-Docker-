from inference.video_model import VideoDeepfakeModel

class ModelContainer:
    def __init__(self):
        self.image = ImageDeepfakeModel()
        self.audio = AudioDeepfakeModel()
        self.text = TextDeepfakeModel()
        self.video = VideoDeepfakeModel(self.image)

    def predict(self, media_type, path_or_text):
        if media_type == "image":
            return self.image.predict(path_or_text)
        elif media_type == "audio":
            return self.audio.predict(path_or_text)
        elif media_type == "text":
            return self.text.predict(path_or_text)
        elif media_type == "video":
            return self.video.predict(path_or_text)
        else:
            raise ValueError("Unsupported media type")

