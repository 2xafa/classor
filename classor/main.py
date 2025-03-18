#!/usr/bin/env python3
import sys
import subprocess
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def ping(ip):
    try:
        subprocess.check_output(['ping', '-c', '1', str(ip)], stderr=subprocess.STDOUT, timeout=1)
        return True
    except:
        return False

def scan_network(network_str):
    try:
        network = ipaddress.ip_network(network_str)
    except ValueError:
        print(f"Hata: Geçersiz ağ adresi. Örnek format: 192.168.1.0/24")
        sys.exit(1)

    print(f"\n{network_str} ağı taranıyor...\n")

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(ping, ip): ip for ip in network.hosts()}
        for future in futures:
            ip = futures[future]
            try:
                if future.result():
                    print(f"{ip} hayatta")
            except:
                continue

def main():
    if len(sys.argv) != 2:
        print("Kullanım: classor <ip_adresi/prefix>")
        print("Örnek: classor 192.168.1.0/24")
        sys.exit(1)

    scan_network(sys.argv[1])

if __name__ == "__main__":
    main()