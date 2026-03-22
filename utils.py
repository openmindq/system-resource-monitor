import psutil
import csv
import logging
import os
from datetime import datetime

# Log dizini oluşturma
LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, 'resources.csv')

def setup_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_resources():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return cpu, memory

def log_to_csv(cpu, memory):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Timestamp', 'CPU_Percent', 'Memory_Percent'])
        writer.writerow([datetime.now().strftime('%Y-%m-%d %H:%M:%S'), cpu, memory])

def check_thresholds(cpu, memory, cpu_threshold, memory_threshold):
    if cpu > cpu_threshold:
        logging.warning(f"Kritik CPU Kullanımı: %{cpu} (Eşik: %{cpu_threshold})")
    if memory > memory_threshold:
        logging.warning(f"Kritik Bellek Kullanımı: %{memory} (Eşik: %{memory_threshold})")
