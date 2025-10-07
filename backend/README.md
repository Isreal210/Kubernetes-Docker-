# Backend – Flask API & Core Logic

The backend is the heart of the Deepfake & Synthetic Media Detector.  
It is responsible for:
- Handling authentication (user signup/login via JWT)
- Managing file uploads and routing data to preprocessing/inference pods
- Storing user results in MongoDB
- Enforcing per-user data isolation and storage limits

