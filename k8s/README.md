# ☸️ Kubernetes Deployment – Deepfake & Synthetic Media Detector

This folder contains all the Kubernetes manifests (YAML files) used to deploy the **Deepfake & Synthetic Media Detector** pipeline.  
Each component — Preprocessing, Inference, Storage, and Backend — runs as a dedicated Pod with defined services, scaling policies, and persistence.  

The setup follows **Infrastructure-as-Code (IaC)** principles for reproducibility and version control.

---

## 🚀 Overview

### 🎯 Objective
Deploy a **multi-pod, multi-container pipeline** that can:
- Accept media uploads securely
- Process and analyze files using machine learning models
- Store and manage user data with privacy and isolation
- Scale dynamically under load (especially inference)

---

## 🧩 Folder Structure

| File | Description |
|------|--------------|
| `preprocessing_deployment.yaml` | Defines the preprocessing pod (image/audio/video/text normalization) and internal service. |
| `inference_deployment.yaml` | Deploys the multi-container inference pod (model container + metrics container). |
| `storage_deployment.yaml` | MongoDB pod for user data, results, and logs. Includes persistence setup with PVC. |
| `backend_deployment.yaml` | Flask API pod for user uploads, authentication, and data routing between components. |
| `pvc.yaml` | Persistent Volume Claim used for storing media files, logs, and MongoDB data. |

---

## 🧱 Architecture Summary

Each component in the pipeline is containerized and deployed as a **Kubernetes Pod**:

| Pod | Description | Service Type |
|------|--------------|---------------|
| **Flask API Pod** | Handles all external HTTP/HTTPS requests from the frontend. Routes data internally to preprocessing and inference. | LoadBalancer |
| **Preprocessing Pod** | Performs all cleaning and normalization tasks for uploaded files before sending them to inference. | ClusterIP |
| **Inference Pod (Multi-Container)** | Hosts AI models for deepfake/synthetic detection (image, audio, video, text). Also includes a metrics container for performance logging. | ClusterIP |
| **Storage Pod** | Runs MongoDB to persist user data, results, and media metadata. | ClusterIP |
| **Frontend Pod (Optional)** | Hosts the React frontend UI (static files served via Nginx). | LoadBalancer |

---

## ⚙️ Persistence Setup

Data persistence is achieved using **Persistent Volume Claims (PVCs)**, defined in `pvc.yaml`.

### 🗂️ Storage Plan
- **MongoDB PVC:** Persistent storage for user profiles, results, and logs.  
- **Preprocessing PVC:** Temporary storage for media files (auto-cleared after inference).  
- **Inference PVC:** Cache and temporary model data storage.  

Each PVC mounts to a shared **Persistent Volume (PV)** defined in the cluster configuration.

---

## 📈 Scaling & Reliability

- The **Inference Pod** is the most compute-intensive and horizontally scalable component.  
- Replicas are managed using a **Kubernetes Deployment** with autoscaling parameters.  
- Health checks (`livenessProbe`, `readinessProbe`) ensure pods recover automatically.  
- Logs are stored centrally via the Storage Pod for debugging and auditing.

---

## 🔐 Security Considerations

- Secrets (e.g., DB credentials, JWT keys) are managed using **Kubernetes Secrets**.  
- Network Policies restrict cross-pod communication to approved namespaces.  
- HTTPS enforced on the LoadBalancer for secure data transmission.  
- User data isolation is maintained through MongoDB access control and token-based authentication.  

---
