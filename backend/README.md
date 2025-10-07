# 🧠 Inference & Backend API – Deepfake & Synthetic Media Detector

This module serves as the **Flask-based backend** for the Deepfake & Synthetic Media Detector.  
It connects the **frontend (React)** to the **core AI models**, handling user authentication, media uploads, preprocessing coordination, and inference results.  
It is designed to be cloud-ready and fully containerized for deployment in a **Kubernetes multi-pod architecture**.

---

## 🚀 Overview

The backend acts as the main controller for:
- User registration, authentication, and session management (JWT-based)
- Upload and routing of media files (images, video, audio, text)
- Calling preprocessing and inference pods for model evaluation
- Returning results and confidence scores to the frontend
- Managing user storage and previously saved uploads

---

## ⚙️ Key Components

| File | Description |
|------|--------------|
| `model_loader.py` | Loads and initializes pretrained models for each media type (text, image, audio, video). |
| `inference_api.py` | Flask REST API endpoints that handle uploads, run inference, and send responses to the frontend. |
| `utils.py` | Helper functions for scoring, logging, and error handling. |
| `requirements.txt` | Dependencies for Python packages such as Flask, TensorFlow/PyTorch, and MongoDB drivers. |

---

## 💾 Data Persistence

MongoDB is used for:
- Storing user profiles and hashed credentials  
- Logging user uploads and detection results  
- Storing user-specific history (with storage limits per account)

Persistent Volumes (PVCs) are used in Kubernetes to handle:
- Temporary file storage for uploaded media  
- Logs and inference results

Each user’s uploads are **private and isolated**. Users can choose whether to store results permanently.  
If their allocated storage is full, they are prompted to clear old results before saving new ones.

---

## 🧱 Deployment Notes

- This Flask service runs as a **single container pod** inside Kubernetes.
- Exposed externally via a **LoadBalancer service** for HTTPS communication.
- Communicates internally with the preprocessing and storage pods via **ClusterIP services**.

---

## 🧪 Testing

Refer to the `/tests` folder for:
- Authentication tests
- Upload/inference flow tests
- Error handling (invalid file, large file, missing token)


