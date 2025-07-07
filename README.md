# Player Re-Identification in Single Feed

This project solves the re-identification problem for players in a single-camera sports feed.

## 🎯 Objective
- Detect players in a 15-second sports video.
- Assign consistent player IDs even when they leave and re-enter the frame.
- Simulate real-time tracking and re-identification.

## 🧩 Approach
- Used YOLOv11 (`best.pt`) for player detection.
- Used DeepSORT tracker for real-time tracking and re-identification.

## 📄 Files
- `main.py` — script to run detection and tracking.
- `best.pt` — YOLOv11 model weights (provided).
- `output.mp4` — generated output video.

## ▶️ How to Run
### 1️⃣ Install dependencies:
```bash
pip install -r requirements.txt
