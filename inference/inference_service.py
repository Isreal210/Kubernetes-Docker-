from flask import Flask, request, jsonify
from model_loader import ModelContainer
import tempfile, os

app = Flask(__name__)
models = ModelContainer()

@app.route("/infer", methods=["POST"])
def infer():
    media_type = request.form.get("media_type")
    if media_type in ["image", "audio", "video"]:
        file = request.files["file"]
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            file.save(tmp.name)
            result = models.predict(media_type, tmp.name)
        os.remove(tmp.name)
    elif media_type == "text":
        text = request.form.get("text")
        result = models.predict("text", text)
    else:
        return jsonify({"error": "Invalid media type"}), 400

    return jsonify({"status": "success", "media_type": media_type, "result": result}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
