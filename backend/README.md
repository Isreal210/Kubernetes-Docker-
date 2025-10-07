# Backend – Flask API & Core Logic

The backend is the heart of the Deepfake & Synthetic Media Detector.  
It is responsible for:
- Handling authentication (user signup/login via JWT)
- Managing file uploads and routing data to preprocessing/inference pods
- Storing user results in MongoDB
- Enforcing per-user data isolation and storage limits

---

## 🧱 Structure

backend/
│
├── app/
│ ├── routes/
│ │ ├── auth_routes.py # Handles user registration and login
│ │ ├── upload_routes.py # Accepts uploads and validates file type
│ │ ├── history_routes.py # Displays user’s previous analysis results
│ │ └── inference_routes.py # Communicates with inference pod
│ ├── models/
│ │ ├── user_model.py # User schema (MongoDB)
│ │ ├── result_model.py # Detection results schema
│ │ └── storage_model.py # Storage tracking per user
│ ├── utils/
│ │ ├── jwt_helper.py # Token creation & verification
│ │ ├── hashing.py # Password hashing and verification
│ │ ├── file_validation.py # Validates size, format, etc.
│ │ └── logger.py # Centralized logging
│ ├── config.py # MongoDB & environment configs
│ └── main.py # Flask app entry point
│
├── requirements.txt
└── README.md
