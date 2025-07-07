# main.py

from ultralytics import YOLO
import cv2
from deep_sort_realtime.deepsort_tracker import DeepSort

# Load YOLOv11 model (weights file downloaded from Drive)
model = YOLO("best.pt")

# Initialize DeepSORT tracker
tracker = DeepSort(max_age=30)

# Input video
video_path = "15sec_input_720p.mp4"
cap = cv2.VideoCapture(video_path)

# Output video
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLOv11 detection
    results = model(frame)

    # Prepare detections for DeepSORT
    detections = []
    for r in results[0].boxes.data:
        x1, y1, x2, y2, conf, cls = r.tolist()
        detections.append([x1, y1, x2, y2, conf, int(cls)])

    # Update tracker
    tracks = tracker.update_tracks(detections, frame=frame)

    # Draw results
    for track in tracks:
        if not track.is_confirmed():
            continue
        track_id = track.track_id
        l, t, r, b = map(int, track.to_ltrb())
        cv2.rectangle(frame, (l, t), (r, b), (0, 255, 0), 2)
        cv2.putText(frame, f"ID: {track_id}", (l, t - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    out.write(frame)
    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
