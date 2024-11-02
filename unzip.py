import zipfile
import tarfile
import os

def extract_archive():
    archive_path = input("Çıkarılacak arşiv dosyasının yolunu girin: ")
    destination_path = input("Dosyaların çıkarılacağı dizinin yolunu girin: ")

    # Hedef dizin yoksa oluştur
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    if archive_path.endswith('.zip'):
        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            zip_ref.extractall(destination_path)
        print(f"{archive_path} başarıyla {destination_path} dizinine çıkarıldı.")
    elif archive_path.endswith(('.tar.gz', '.tgz', '.tar', '.tar.bz2')):
        with tarfile.open(archive_path, 'r:*') as tar_ref:
            tar_ref.extractall(destination_path)
        print(f"{archive_path} başarıyla {destination_path} dizinine çıkarıldı.")
    else:
        print("Desteklenmeyen arşiv türü. Lütfen .zip veya .tar.* formatında bir dosya seçin.")

extract_archive()

