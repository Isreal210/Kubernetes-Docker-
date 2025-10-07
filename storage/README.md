# Storage Service (MongoDB + Persistent Volumes)

The storage service handles all data persistence.  
It stores user profiles, model results, logs, and optional stored uploads.

---

## 🧩 Key Features
- MongoDB for structured data (Users, Results, Storage Quotas)
- PVC-backed storage for media/logs
- User data isolation — only owners can view their uploads
- Automatic cleanup once storage quota is full

---

## ⚙️ Collections
| Collection | Description |
|-------------|-------------|
| `users` | Stores username, hashed password, and metadata |
| `results` | Stores each media result tied to a user |
| `logs` | System-level logging for auditing |

---

## 🔒 Security
- Per-user storage access enforcement
- Encrypted credentials in Secrets
- Volume cleanup routine to respect user limits
