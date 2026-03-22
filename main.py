import psutil
import time
import logging

# Loglama ayarları
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_system_resources():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    logging.info(f"CPU Kullanımı: {cpu_usage}%")
    logging.info(f"Bellek (RAM) Kullanımı: {memory_usage}%")

if __name__ == "__main__":
    print("Sistem İzleyici Başlatıldı (Çıkış için Ctrl+C)")
    try:
        while True:
            log_system_resources()
            time.sleep(5)  # 5 saniyede bir kontrol et
    except KeyboardInterrupt:
        print("\nİzleyici durduruldu.")
