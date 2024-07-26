from ultralytics import YOLO


model = YOLO('yolov8n.pt') 
model.train(data="C:/Users/Özgür/Desktop/dataset/dataset/dataset.yaml", epochs=100, imgsz=640)
model.save('C:/Users/Özgür/Desktop/dataset/yolov8n.pt')
