import cv2
from ultralytics import YOLO

def main():
    # YOLO modelini yükle
    model = YOLO('yolov8n.pt')

    # Kamerayı başlat
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Modeli kullanarak tahmin yap
        results = model(frame)

        # Sonuçları görselleştir
        annotated_frame = results[0].plot()

        # Sonuçları ekranda göster
        cv2.imshow('YOLOv8 Cinsiyet Tanıma', annotated_frame)

        # 'q' tuşuna basarak çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Kaynakları serbest bırak
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
