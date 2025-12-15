import psutil  # components info
import time
import socket  # machine info
import platform  # os info
import os
from pathlib import Path
from datetime import datetime


path = Path.home() / "Desktop/projetAAA-main"
ext = ('.txt', '.py', '.pdf', '.jpg')

def get_primary_ip():
    req = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        req.connect(("8.8.8.8", 80))
        return req.getsockname()[0]
    finally:
        req.close()

def format_bytes(bytes_value):
    gb = bytes_value / (1024 ** 3)
    return round(gb, 2)

def format_uptime(seconds):
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{days}d {hours}h {minutes}m"

# Initialize CPU monitoring
psutil.cpu_percent()
for p in psutil.process_iter():
    try:
        p.cpu_percent()
    except:
        pass
        
print("script is running")

while True:
    # sysinfo
    name = socket.gethostname()
    os_name = platform.system()
    os_version = platform.release()
    os_full = f"{os_name} {os_version}"

    boot_timestamp = psutil.boot_time()
    current_time = time.time()
    uptime_seconds = current_time - boot_timestamp
    uptime = format_uptime(uptime_seconds)
    boot_time = datetime.fromtimestamp(boot_timestamp).strftime('%Y-%m-%d %H:%M:%S')
    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    users = psutil.users()
    user_count = len(users)
    user_names = ", ".join([u.name for u in users]) if users else "None"

    # CPU
    cores = psutil.cpu_count()
    cores_logical = psutil.cpu_count(logical=True)
    cores_physical = psutil.cpu_count(logical=False)

    clock_rate = psutil.cpu_freq()
    curr_cl = round(clock_rate.current, 2)
    min_cl = round(clock_rate.min, 2)
    max_cl = round(clock_rate.max, 2)

    cpu_percent = psutil.cpu_percent()
    cpu_per_core = psutil.cpu_percent(percpu=True)
    
    # RAM
    ram = psutil.virtual_memory()
    total_ram = ram.total
    total_ram_gb = format_bytes(total_ram)
    in_use = ram.used
    in_use_gb = format_bytes(in_use)
    available_ram = ram.available
    available_ram_gb = format_bytes(available_ram)
    percent_ram = round(ram.percent, 2)
    
    # DISK
    disk = psutil.disk_usage('/')
    total_disk = disk.total
    total_disk_gb = format_bytes(total_disk)
    used_disk = disk.used
    used_disk_gb = format_bytes(used_disk)
    free_disk = disk.free
    free_disk_gb = format_bytes(free_disk)
    percent_disk = round(disk.percent, 2)
    
    # IP
    main_ip = get_primary_ip()

    # PROCESSES
    processes = []
    process_count = 0
    for p in psutil.process_iter(['pid', 'name', 'memory_percent', 'status']):
        try:
            process_count += 1
            cpu_use = p.cpu_percent()
            processes.append({
                'pid': p.pid,
                'name': p.name(),
                'cpu_percent': cpu_use,
                'memory_percent': p.info['memory_percent'],
                'status': p.info['status']
            })
        except:
            pass

    top3_cpu = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)[:3]
    top3_ram = sorted(processes, key=lambda x: x['memory_percent'], reverse=True)[:3]
    top3 = sorted(processes, key=lambda x: x['cpu_percent'] + x['memory_percent'], reverse=True)[:3]

    cpu_pid1 = top3_cpu[0]['pid']
    cpu_pid2 = top3_cpu[1]['pid']
    cpu_pid3 = top3_cpu[2]['pid']
    cpu_name1 = top3_cpu[0]['name']
    cpu_name2 = top3_cpu[1]['name']
    cpu_name3 = top3_cpu[2]['name']
    cpu_memory1 = round(top3_cpu[0]['memory_percent'], 2)
    cpu_memory2 = round(top3_cpu[1]['memory_percent'], 2)
    cpu_memory3 = round(top3_cpu[2]['memory_percent'], 2)
    cpu_cpu1 = round(top3_cpu[0]['cpu_percent'], 2)
    cpu_cpu2 = round(top3_cpu[1]['cpu_percent'], 2)
    cpu_cpu3 = round(top3_cpu[2]['cpu_percent'], 2)

    ram_pid1 = top3_ram[0]['pid']
    ram_pid2 = top3_ram[1]['pid']
    ram_pid3 = top3_ram[2]['pid']
    ram_name1 = top3_ram[0]['name']
    ram_name2 = top3_ram[1]['name']
    ram_name3 = top3_ram[2]['name']
    ram_memory1 = round(top3_ram[0]['memory_percent'], 2)
    ram_memory2 = round(top3_ram[1]['memory_percent'], 2)
    ram_memory3 = round(top3_ram[2]['memory_percent'], 2)
    ram_cpu1 = round(top3_ram[0]['cpu_percent'], 2)
    ram_cpu2 = round(top3_ram[1]['cpu_percent'], 2)
    ram_cpu3 = round(top3_ram[2]['cpu_percent'], 2)

    top_pid1 = top3[0]['pid']
    top_pid2 = top3[1]['pid']
    top_pid3 = top3[2]['pid']
    top_name1 = top3[0]['name']
    top_name2 = top3[1]['name']
    top_name3 = top3[2]['name']
    top_memory1 = round(top3[0]['memory_percent'], 2)
    top_memory2 = round(top3[1]['memory_percent'], 2)
    top_memory3 = round(top3[2]['memory_percent'], 2)
    top_cpu1 = round(top3[0]['cpu_percent'], 2)
    top_cpu2 = round(top3[1]['cpu_percent'], 2)
    top_cpu3 = round(top3[2]['cpu_percent'], 2)

    # Analyze folder
    files = [p for p in path.iterdir() if p.is_file()]
    files_name = [p.name for p in files]
    total_files_count = len(files)
    directory_size = sum(p.stat().st_size for p in files)
    directory_size_mb = round(directory_size / (1024 ** 2), 2)
    
    # Count by extension
    txt_files = [p.name for p in files if p.suffix == '.txt']
    py_files = [p.name for p in files if p.suffix == '.py']
    pdf_files = [p.name for p in files if p.suffix == '.pdf']
    jpg_files = [p.name for p in files if p.suffix == '.jpg']
    
    txt_count = len(txt_files)
    py_count = len(py_files)
    pdf_count = len(pdf_files)
    jpg_count = len(jpg_files)
    
    # Calculate percentages
    txt_percent = round((txt_count / total_files_count * 100), 2) if total_files_count > 0 else 0
    py_percent = round((py_count / total_files_count * 100), 2) if total_files_count > 0 else 0
    pdf_percent = round((pdf_count / total_files_count * 100), 2) if total_files_count > 0 else 0
    jpg_percent = round((jpg_count / total_files_count * 100), 2) if total_files_count > 0 else 0
    
    files_with_set_ext = txt_files + py_files + pdf_files + jpg_files
    set_files_count = len(files_with_set_ext)

    with open("template.html", "r") as f:
        html = f.read()

    html = html.replace("{{NAME}}", str(name))
    html = html.replace("{{OS_NAME}}", str(os_name))
    html = html.replace("{{OS_VERSION}}", str(os_version))
    html = html.replace("{{OS_FULL}}", str(os_full))
    html = html.replace("{{UPTIME}}", str(uptime))
    html = html.replace("{{UPTIME_SECONDS}}", str(uptime_seconds))
    html = html.replace("{{BOOT_TIME}}", str(boot_time))
    html = html.replace("{{CURRENT_TIMESTAMP}}", str(current_timestamp))
    html = html.replace("{{USER_COUNT}}", str(user_count))
    html = html.replace("{{USER_NAMES}}", str(user_names))
    html = html.replace("{{CORES}}", str(cores))
    html = html.replace("{{CORES_LOGICAL}}", str(cores_logical))
    html = html.replace("{{CORES_PHYSICAL}}", str(cores_physical))
    html = html.replace("{{CURR_CL}}", str(curr_cl))
    html = html.replace("{{MIN_CL}}", str(min_cl))
    html = html.replace("{{MAX_CL}}", str(max_cl))
    html = html.replace("{{CPU}}", str(cpu_percent))
    html = html.replace("{{CPU_PER_CORE}}", str(cpu_per_core))
    html = html.replace("{{TOTAL_RAM}}", str(total_ram))
    html = html.replace("{{TOTAL_RAM_GB}}", str(total_ram_gb))
    html = html.replace("{{IN_USE}}", str(in_use))
    html = html.replace("{{IN_USE_GB}}", str(in_use_gb))
    html = html.replace("{{AVAILABLE_RAM}}", str(available_ram))
    html = html.replace("{{AVAILABLE_RAM_GB}}", str(available_ram_gb))
    html = html.replace("{{PERCENT_RAM}}", str(percent_ram))
    html = html.replace("{{TOTAL_DISK}}", str(total_disk))
    html = html.replace("{{TOTAL_DISK_GB}}", str(total_disk_gb))
    html = html.replace("{{USED_DISK}}", str(used_disk))
    html = html.replace("{{USED_DISK_GB}}", str(used_disk_gb))
    html = html.replace("{{FREE_DISK}}", str(free_disk))
    html = html.replace("{{FREE_DISK_GB}}", str(free_disk_gb))
    html = html.replace("{{PERCENT_DISK}}", str(percent_disk))
    html = html.replace("{{MAIN_IP}}", str(main_ip))
    html = html.replace("{{PROCESS_COUNT}}", str(process_count))
    html = html.replace("{{RAM_PID1}}", str(ram_pid1))
    html = html.replace("{{RAM_PID2}}", str(ram_pid2))
    html = html.replace("{{RAM_PID3}}", str(ram_pid3))
    html = html.replace("{{RAM_NAME1}}", str(ram_name1))
    html = html.replace("{{RAM_NAME2}}", str(ram_name2))
    html = html.replace("{{RAM_NAME3}}", str(ram_name3))
    html = html.replace("{{RAM_MEMORY1}}", str(ram_memory1))
    html = html.replace("{{RAM_MEMORY2}}", str(ram_memory2))
    html = html.replace("{{RAM_MEMORY3}}", str(ram_memory3))
    html = html.replace("{{RAM_CPU1}}", str(ram_cpu1))
    html = html.replace("{{RAM_CPU2}}", str(ram_cpu2))
    html = html.replace("{{RAM_CPU3}}", str(ram_cpu3))
    html = html.replace("{{CPU_PID1}}", str(cpu_pid1))
    html = html.replace("{{CPU_PID2}}", str(cpu_pid2))
    html = html.replace("{{CPU_PID3}}", str(cpu_pid3))
    html = html.replace("{{CPU_NAME1}}", str(cpu_name1))
    html = html.replace("{{CPU_NAME2}}", str(cpu_name2))
    html = html.replace("{{CPU_NAME3}}", str(cpu_name3))
    html = html.replace("{{CPU_MEMORY1}}", str(cpu_memory1))
    html = html.replace("{{CPU_MEMORY2}}", str(cpu_memory2))
    html = html.replace("{{CPU_MEMORY3}}", str(cpu_memory3))
    html = html.replace("{{CPU_CPU1}}", str(cpu_cpu1))
    html = html.replace("{{CPU_CPU2}}", str(cpu_cpu2))
    html = html.replace("{{CPU_CPU3}}", str(cpu_cpu3))
    html = html.replace("{{TOP_PID1}}", str(top_pid1))
    html = html.replace("{{TOP_PID2}}", str(top_pid2))
    html = html.replace("{{TOP_PID3}}", str(top_pid3))
    html = html.replace("{{TOP_NAME1}}", str(top_name1))
    html = html.replace("{{TOP_NAME2}}", str(top_name2))
    html = html.replace("{{TOP_NAME3}}", str(top_name3))
    html = html.replace("{{TOP_MEMORY1}}", str(top_memory1))
    html = html.replace("{{TOP_MEMORY2}}", str(top_memory2))
    html = html.replace("{{TOP_MEMORY3}}", str(top_memory3))
    html = html.replace("{{TOP_CPU1}}", str(top_cpu1))
    html = html.replace("{{TOP_CPU2}}", str(top_cpu2))
    html = html.replace("{{TOP_CPU3}}", str(top_cpu3))
    html = html.replace("{{FILES_NAME}}", str(files_name))
    html = html.replace("{{TOTAL_FILES_COUNT}}", str(total_files_count))
    html = html.replace("{{SET_FILES_COUNT}}", str(set_files_count))
    html = html.replace("{{DIRECTORY_SIZE}}", str(directory_size))
    html = html.replace("{{DIRECTORY_SIZE_MB}}", str(directory_size_mb))
    html = html.replace("{{FILES_WITH_SET_EXT}}", str(files_with_set_ext))
    html = html.replace("{{PATH}}", str(path))
    html = html.replace("{{TXT_COUNT}}", str(txt_count))
    html = html.replace("{{PY_COUNT}}", str(py_count))
    html = html.replace("{{PDF_COUNT}}", str(pdf_count))
    html = html.replace("{{JPG_COUNT}}", str(jpg_count))
    html = html.replace("{{TXT_PERCENT}}", str(txt_percent))
    html = html.replace("{{PY_PERCENT}}", str(py_percent))
    html = html.replace("{{PDF_PERCENT}}", str(pdf_percent))
    html = html.replace("{{JPG_PERCENT}}", str(jpg_percent))

    with open("index.html", "w") as f:
        f.write(html)

    time.sleep(1)
