import urllib.request
import os

# Create models directory if it doesn't exist
os.makedirs("models", exist_ok=True)

# YOLO model URLs
model_urls = {
    
    "yolov6s.pt": "https://github.com/meituan/YOLOv6/releases/download/0.2.0/yolov6s.pt"
}

# Download models
for model_name, url in model_urls.items():
    print(f"Downloading {model_name}...")
    urllib.request.urlretrieve(url, f"models/{model_name}")
    print(f"{model_name} downloaded successfully.")
