import os
import subprocess

def prepare_dataset():
    # Veri setini hazırlama işlemleri
    dataset_dir = 'dataset'
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    
    men_dir = os.path.join(dataset_dir, 'MEN')
    women_dir = os.path.join(dataset_dir, 'WOMEN')
    
    if not os.path.exists(men_dir):
        print("Lütfen 'MEN' klasörünü dataset klasörüne ekleyin.")
        return False
    
    if not os.path.exists(women_dir):
        print("Lütfen 'WOMEN' klasörünü dataset klasörüne ekleyin.")
        return False
    
    return True

def run_training():
    # Eğitim işlemleri
    try:
        subprocess.run(["python", "verieğitimi.py"])
    except Exception as e:
        print(f"Eğitim sırasında bir hata oluştu: {str(e)}")

def start_camera():
    # Kamera işlemleri
    try:
        subprocess.run(["python", "kamera.py"])
    except Exception as e:
        print(f"Kamera başlatma sırasında bir hata oluştu: {str(e)}")

def main():
    # Ana iş mantığı
    if prepare_dataset():
        run_training()
        start_camera()

if __name__ == "__main__":
    main()
