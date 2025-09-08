# Test Cases

## Purpose
This folder contains test scripts to validate the deepfake detection pipeline. Tests ensure preprocessing, inference, and storage functions work correctly and handle edge cases.

## What Each File Does
- **test_upload_valid.py** – Tests normal uploads (images, videos, audio, text).  
- **test_upload_invalid.py** – Tests corrupted or unsupported files.  
- **test_preprocessing.py** – Verifies preprocessing outputs for each media type.  
- **test_inference.py** – Checks if inference API returns expected results.  
