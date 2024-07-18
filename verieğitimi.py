import os
import shutil
import random

def prepare_data(src_dir, dest_dir, val_split=0.2):
    # Veri hazırlama işlemleri
    images = [f for f in os.listdir(src_dir) if f.endswith('.jpg') or f.endswith('.png')]
    random.shuffle(images)

    split_index = int(len(images) * (1 - val_split))
    train_images = images[:split_index]
    val_images = images[split_index:]

    for img in train_images:
        shutil.copy(os.path.join(src_dir, img), os.path.join(dest_dir, 'train', img))

    for img in val_images:
        shutil.copy(os.path.join(src_dir, img), os.path.join(dest_dir, 'val', img))

if __name__ == "__main__":
    # Veri seti klasörleri
    dataset_dir = 'dataset'
    source_dir = os.path.join(dataset_dir, 'source')
    dest_dir = os.path.join(dataset_dir, 'processed')
    
    # Gerekli klasörleri oluştur
    os.makedirs(os.path.join(dest_dir, 'train'), exist_ok=True)
    os.makedirs(os.path.join(dest_dir, 'val'), exist_ok=True)
    
    # Veri hazırlama işlemlerini yap
    prepare_data(source_dir, dest_dir)
