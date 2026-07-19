import socket
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

open_ports = []
target = input("Target IP/domain: ")
while True:
    max = int(input("Max port to scan(1-65535): "))
    if max < 1 or max > 65535:
        print("Invalid max port. Please enter a number between 1 and 65535.")
    else:
        break

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except OSError:
            service = "unknown"
        
        open_ports.append((port, service))
        print(f"Port {port}: OPEN ({service})")
    
    sock.close()

start_time = datetime.now()
print(f"start scan: {start_time}")

with ThreadPoolExecutor(max_workers=50) as executor:
    executor.map(scan_port, range(1, max+1))

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

print(f"\nscan completed! Results saved to {filename}")