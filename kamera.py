import cv2
from ultralytics import YOLO


model = YOLO('C:/Users/Özgür/Desktop/dataset/yolov8n.pt') 
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    
    results = model(frame)

    
    for result in results:
        for box in result.boxes:
            
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            
            
            if cls == 0 or cls == 1:  
                label = 'Male' if cls == 0 else 'Female'
                   
                center_x = (x1 + x2) // 3
                center_y = (y1 + y2) // 3

               
                print(f"Box coordinates: ({x1}, {y1}), ({x2}, {y2})")
                print(f"Confidence: {conf}, Class: {cls}, Label: {label}")

                
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 4)  
                cv2.putText(frame, f'{label} {conf:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (36, 255, 12), 1)  

   
    cv2.imshow('Gender Detection', frame)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
