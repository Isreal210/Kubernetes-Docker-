# 🧹 Preprocessing Module – Deepfake & Synthetic Media Detector

This module is responsible for preparing all uploaded media before inference.  
It ensures that videos, images, audio, and text files are normalized, sanitized, and formatted correctly before being sent to the inference models.  

All preprocessing runs inside its own **Kubernetes Pod**, isolated from public access for security.  

---

## 🚀 Overview

The preprocessing service standardizes different types of media so that they can be safely analyzed by AI models.  
Each media type follows a specific workflow:

| Media Type | Preprocessing Steps |
|-------------|--------------------|
| **Video** | Extract frames → Resize → Normalize pixel data → Compress for inference |
| **Image** | Resize → Normalize pixel intensity → Convert to model input tensor |
| **Audio** | Convert waveform → Generate Mel-spectrogram → Normalize amplitude |
| **Text** | Tokenize → Remove stopwords → Normalize punctuation/case |

The output of each process is passed to the **Inference Pod** for classification.

---

## 🧩 File Structure

| File | Description |
|------|--------------|
| `video_preprocessing.py` | Extracts frames from uploaded video files and prepares them for the video deepfake model. |
| `audio_preprocessing.py` | Converts uploaded audio into spectrograms compatible with the speech detection model. |
| `text_preprocessing.py` | Cleans, tokenizes, and prepares textual data for AI-generated text detection. |
| `helpers.py` | Common utility functions used across preprocessing modules (e.g., file validation, format conversion). |

---

## 🧠 Core Logic

Each script:
1. Validates the uploaded file type and size.  
2. Extracts and normalizes the data.  
3. Saves temporary preprocessed outputs in a shared volume for inference.  
4. Sends a signal or API request to the **Inference Pod** for processing.  

Temporary files are deleted after inference unless the user chooses to store them.

---

## 🧱 Kubernetes Integration

- Runs as a **single-container Pod** inside Kubernetes.  
- Communicates internally via a **ClusterIP Service** to the inference pod.  
- Uses a shared **Persistent Volume Claim (PVC)** for temporary media storage.  
- Isolates untrusted uploads from direct user access for security.

---

## 🔐 Security & Validation

- Input validation checks file extensions and MIME types.  
- Size limits enforced (e.g., 100MB max).  
- Corrupted or malformed files trigger standardized error messages.  
- Sanitization ensures user-uploaded text or metadata cannot trigger code injection.  

All operations are logged and sent to the **Storage Pod**
