# Inference Module

## Purpose
This folder is for the core deepfake detection logic. It handles model loading, running predictions, and exposing an API endpoint for user uploads.

## What Each File Does
- **model_loader.py** – Loads pre-trained deepfake detection models (image, video, audio, text).  
- **inference_api.py** – Provides API endpoints (FastAPI or Flask) to accept user media and return “Real” or “Fake” with a confidence score.  
- **utils.py** – Helper functions for formatting results, calculating confidence, or post-processing outputs.  
- **requirements.txt** – Python dependencies needed for inference.  
