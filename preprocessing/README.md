# Preprocessing Module

## Purpose
This folder contains all scripts and utilities responsible for preparing media for deepfake detection. Preprocessing ensures that videos, audio, images, and text are converted into formats suitable for inference models.

## What Each File Does
- **video_preprocessing.py** – Extracts frames from video files, resizes, and normalizes them for the model.  
- **audio_preprocessing.py** – Converts audio files into spectrograms or other model-friendly representations.  
- **text_preprocessing.py** – Cleans and tokenizes text, preparing it for analysis.  
- **helpers.py** – Utility functions like file validation, format checks, and error handling.  
