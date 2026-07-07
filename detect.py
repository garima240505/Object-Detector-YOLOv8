import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

print("Loading YOLO model...")
model = YOLO("yolov8n.pt")


print("Reading image...")
image = cv2.imread("images/dog.jpg")


if image is None:
    print("Error: Could not read the image.")
    exit()

print("Detecting objects...")
results = model(image)


print("Drawing bounding boxes...")
annotated_image = results[0].plot()
cv2.imwrite("output/detected_dog.jpg", annotated_image)

print("Output image saved successfully!")

annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)


plt.imshow(annotated_image)
plt.title("YOLOv8 Object Detection")
plt.axis("off")
plt.show()

print("Done!")