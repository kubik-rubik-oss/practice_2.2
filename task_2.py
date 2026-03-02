import psutil
import time

while True:
    cpu = psutil.cpu_percent(interval = 1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"\rЗагрузка CPU за 1 сек.: {cpu}% - Использование RAM: {ram}% - Использование диска: {disk}%", end='')

    time.sleep(1)