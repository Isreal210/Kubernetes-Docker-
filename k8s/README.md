# Kubernetes Deployment

## Purpose
This folder contains all Kubernetes manifests needed to deploy the deepfake detection pipeline. It defines pods, services, and persistent storage for media and logs.

## What Each File Does
- **preprocessing_deployment.yaml** – Deployment and Service for preprocessing pod.  
- **inference_deployment.yaml** – Deployment and Service for inference pod.  
- **storage_deployment.yaml** – Deployment and Service for storage/alert pod.  
- **pvc.yaml** – Defines Persistent Volume Claims for storing uploaded media and logs.  
