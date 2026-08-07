import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt")

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Webcam could not be opened.")
    exit()

print("Detection started. Press Q to stop.")

while True:
    success, frame = camera.read()

    if not success:
        print("Unable to read webcam frame.")
        break

    results = model.predict(
        source=frame,
        conf=0.4,
        verbose=False
    )

    detected_frame = results[0].plot()

    cv2.imshow("YOLO Object Detection", detected_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()