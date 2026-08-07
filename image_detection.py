from pathlib import Path

from ultralytics import YOLO


model = YOLO("yolov8n.pt")

input_folder = Path("input_images")
output_folder = Path("output_images")

output_folder.mkdir(exist_ok=True)

supported_formats = {".jpg", ".jpeg", ".png"}

for image_path in input_folder.iterdir():
    if image_path.suffix.lower() not in supported_formats:
        continue

    print(f"Detecting objects in: {image_path.name}")

    model.predict(
        source=str(image_path),
        conf=0.4,
        save=True,
        project=str(output_folder),
        name="results",
        exist_ok=True
    )

print("Detection completed.")
print("Check the output_images/results folder.")