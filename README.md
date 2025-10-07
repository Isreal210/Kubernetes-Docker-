# 🧪 Testing & Validation – Deepfake & Synthetic Media Detector

This folder contains all **unit, integration, and system tests** for the Deepfake & Synthetic Media Detector project.  
The goal of this testing suite is to ensure the reliability, performance, and security of the end-to-end media processing pipeline — from upload to inference to storage.

---

## 🚀 Overview

The testing process is divided into multiple stages to match the **multi-pod Kubernetes architecture**:

| Test Level | Description |
|-------------|--------------|
| **Unit Tests** | Validate individual functions and preprocessing logic (e.g., image resizing, text cleaning). |
| **Integration Tests** | Test interactions between pods (Flask API ↔ Preprocessing ↔ Inference ↔ Storage). |
| **System Tests** | Simulate real user scenarios: upload → analyze → store → retrieve. |
| **Security Tests** | Validate authentication, authorization, and data isolation per user. |

---

## 🧩 Folder Structure

| File | Description |
|------|--------------|
| `test_upload_valid.py` | Tests valid file uploads and successful inference results. |
| `test_upload_invalid.py` | Tests unsupported or corrupted files and expected error messages. |
| `test_inference.py` | Validates that models load correctly and inference returns accurate predictions. |
| `test_preprocessing.py` | Ensures preprocessing modules (audio, video, text, image) produce expected outputs. |
| `test_authentication.py` | Confirms JWT-based authentication flow (register → login → token validation). |
| `test_storage.py` | Verifies that user data persists correctly in MongoDB and can be cleared when full. |

