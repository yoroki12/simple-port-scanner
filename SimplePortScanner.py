import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from tqdm import tqdm

check = 0
open_ports = []


while True:
    target = input("Target IP/domain: ")
    
    try: 
        ipaddress.ip_address(target)
        ip = target
        check += 1
        break
    except ValueError:
        try:
            ip = socket.gethostbyname(target)
            break
        except socket.gaierror:
            print ("Invalid ip or domain")

while True:
    max = int(input("Max port to scan(1-65535): "))
    if max < 1 or max > 65535:
        print("Invalid max port. Please enter a number between 1 and 65535.")
    else:
        break

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "unknown"
        
        open_ports.append((port, service))
        tqdm.write(f"Port {port}: OPEN ({service})")    
    sock.close()

start_time = datetime.now()
print(f"start scan: {start_time}")

with ThreadPoolExecutor(max_workers=50) as executor:
    list(tqdm(
        executor.map(scan_port, range(1, max + 1)),
        total=max,
        desc="Scanning Ports",
        unit="port"
    ))

end_time = datetime.now()
open_ports.sort() 

filename = f"scan_result_{target}.txt"
with open(filename, "w") as f:
    f.write(f"Port Scan Report\n")
    f.write(f"Target: {target}\n")
    f.write(f"Start time: {start_time}\n")
    f.write(f"End time: {end_time}\n")
    f.write(f"Duration: {end_time - start_time}\n")
    f.write(f"\nOpen ports:\n")
    for port, service in open_ports:
        f.write(f"  Port {port}: {service}\n")
    f.write(f"\nTotal open ports: {len(open_ports)}\n")
    if check == 0:
        f.write(f"IP Address: {ip}\n")
    else:
        pass

print(f"\nscan completed! Results saved to {filename}")