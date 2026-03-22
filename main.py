import json
import time
import utils

# Konfigürasyon yükle
with open('config.json', 'r') as f:
    config = json.load(f)

if __name__ == "__main__":
    utils.setup_logging()
    print("Sistem İzleyici Başlatıldı (Çıkış için Ctrl+C)")
    
    try:
        while True:
            cpu, memory = utils.get_resources()
            
            # Verileri CSV'ye logla
            utils.log_to_csv(cpu, memory)
            
            # Eşikleri kontrol et ve uyar
            utils.check_thresholds(cpu, memory, config['cpu_threshold'], config['memory_threshold'])
            
            time.sleep(config['monitor_interval'])
    except KeyboardInterrupt:
        print("\nİzleyici durduruldu.")
