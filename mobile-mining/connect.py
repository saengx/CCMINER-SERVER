import os, time, json
import requests
def autoconnect(url, filename):
 try:
     with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             ip = loads['ip']            
             USER = f"{ip}"
      
             url = f"https://raw.githubusercontent.com/{USER}/miner/main/process.json"
             output_filename = "setip/ip.json"
             response = requests.get (url, stream=True)
             response.raise_for_status() 
     with open(filename, 'wb') as f:
         for chunk in response.iter_content(chunk_size=8192):
             f.write(chunk)
             print(f"\n\033[93m{url}\033[0m\n")
             print("\033[1;33;40m")
             os.system("figlet -f ANSI_Shadow run-miner")
             print("\033[00m\n")

 except requests.exceptions.RequestException as e:
             print ("\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m\n")
             time.sleep(10)
             os.system ("python3 connect.py")

with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             ip = loads['ip']
            
             USER = f"{io}"
            
url_to_download = f"https://raw.githubusercontent.com/{USER}/miner/main/process.json"
output_filename = "setip/ip.json"
autoconnect(url_to_download, output_filename)