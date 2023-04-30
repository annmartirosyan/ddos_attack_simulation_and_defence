import psutil
import datetime
import time

while True:
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_io = psutil.disk_io_counters().read_count
    network_connections = len(psutil.net_connections())

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("system_monitor.txt", "a") as f:
        f.write(f"{timestamp} | CPU: {cpu_usage}% | RAM: 
{ram_usage}% | >

    time.sleep(1)
