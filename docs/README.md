# 📘 Documentation – Deepfake & Synthetic Media Detector

This folder contains all the design and planning documentation for the **Deepfake & Synthetic Media Detector** project.  
It includes architectural diagrams, data flow visualizations, and planning materials required for Milestone 1 and future implementation phases.

---

## 🧩 Purpose
The goal of this documentation folder is to capture all conceptual and design-related artifacts for the project before deployment.  
This ensures clarity, version tracking, and alignment between all team members working on different pods (Preprocessing, Inference, Backend, etc.).

---

## 📂 Contents
| File | Description |
|------|--------------|
| `data_flow_diagram.png` | Illustrates how user uploads move through the system (upload → preprocessing → inference → storage → response). |
| `architecture_diagram.png` | Shows the Kubernetes pod layout and service communication. |
| `test_plan.md` | Contains test case design, success/failure criteria, and validation approach. |
| `risk_register.md` | Identifies project risks and proposed mitigations. |
| `user_stories.md` | 2–3 realistic user stories based on target audiences. |
| `api_contracts.md` | Lists REST endpoints, input/output examples, and response codes. |

---

## 🧠 Key Design Goals
- Modular and **cloud-native** Kubernetes architecture  
- Secure authentication and **per-user data isolation**  
- Horizontal scalability for inference workloads  
- Transparent data flow documentation and traceability

---

## 📜 Notes
All files in this folder should be version-controlled and reviewed by at least one other team member before merging into the main branch.  
Each document should reflect real system behavior as the project evolves (no placeholders in final versions).

---

## 🧑‍💻 Maintainers
This documentation is maintained by:
- **Kevin Ha** – Lead / PM  
- **Isreal Adegbie** – DevOps  
- **Thomas Burke** – Frontend / Preprocessing  
- **Mo Abdularazzak** – Backend  
- **Alym Rejepov** – Backend  
