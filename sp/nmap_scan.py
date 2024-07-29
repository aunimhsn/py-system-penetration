# Need https://nmap.org/download.html#windows
import nmap3
import json

nmap = nmap3.Nmap()

for i in range(1, 255):
    print(f'Scanning IP : 192.168.56.{i}')

    results = nmap.scan_top_ports(f'192.168.56.{i}')
    if not results[f'192.168.56.{i}']['state']['state'] == 'down':
        with open(f"reports/results-192-168-56-{i}.json", "w") as file: 
            json.dump(results, file, indent=4)