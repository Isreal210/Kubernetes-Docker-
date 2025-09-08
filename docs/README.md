# Deepfake & Synthetic Media Detector

## Project Overview
The Deepfake & Synthetic Media Detector is a Kubernetes-based pipeline designed to help users detect AI-generated or manipulated media, including images, videos, audio, and text. Users upload media, which is processed through a multi-pod pipeline to classify content as "Real" or "Fake," providing confidence scores and logging results. This project emphasizes infrastructure as code, multi-pod orchestration, and persistence handling in Kubernetes.

## Project Goal
- Empower users to detect deepfakes and synthetic media.
- Demonstrate multi-pod and multi-container Kubernetes deployment.
- Implement preprocessing, inference, storage, and alerting in a structured pipeline.
- Provide real-time detection and logging for potential misinformation.
