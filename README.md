# player-reid-assignment
🎬 Player Re-Identification in Single-Camera Sports Feed
This project is part of the internship assignment for Liat.ai.
The goal is to solve the player re-identification problem in a single sports video feed, ensuring that each player maintains a consistent ID even when leaving and re-entering the frame.
The solution simulates real-time processing on a 15-second sports video using modern detection and tracking techniques.

🧩 Approach
🔍 Detection: YOLOv11 (fine-tuned for player & ball detection) — provided best.pt weights.

🚶 Tracking & Re-Identification: DeepSORT tracker, which assigns and maintains IDs based on appearance and motion cues.

🖼️ Outputs an annotated video (output.mp4) with bounding boxes and consistent player IDs.

📥 Data & Weights
✅ YOLOv11 weights: best.pt — download and place in the root directory.

❌ Input video (15sec_input_720p.mp4) is expected but not included in the provided materials — please contact the company to obtain it.
