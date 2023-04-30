import psutil
import datetime
import time

while True:
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_io = psutil.disk_io_counters()
    disk_read_count = disk_io.read_count
    disk_write_count = disk_io.write_count
    disk_read_bytes = disk_io.read_bytes
    disk_write_bytes = disk_io.write_bytes
    disk_read_time = disk_io.read_time
    disk_write_time = disk_io.write_time
    disk_busy_time = disk_io.busy_time
    disk_read_merged_count = disk_io.read_merged_count
    disk_write_merged_count = disk_io.write_merged_count
    network_connections = len(psutil.net_connections())

    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("system_monitor.txt", "a") as f:
        f.write(f"{timestamp} | CPU: {cpu_usage}% | RAM: {ram_usage}% | Disk Read Count: {disk_read_count} | Disk Write Count: {disk_write_count} | Disk Read Bytes: {disk_read_bytes} | Disk Write Bytes: {disk_write_bytes} | Disk Read Time: {disk_read_time} | Disk Write Time: {disk_write_time} | Disk Busy Time: {disk_busy_time} | Disk Read Merged Count: {disk_read_merged_count} | Disk Write Merged Count: {disk_write_merged_count} | Network Connections: {network_connections}\n")

    time.sleep(1)
