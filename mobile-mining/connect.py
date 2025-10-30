import os, time, json
import requests
def autoconnect(url, filename):
 try:
     with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             user = loads['user']
             file = loads['file']
             USER = f"{user}"
             FILE = f"{file}"
             print("\033[1;32;40m")
             os.system("figlet -f digital SETTING")
             print("\033[00m\n")
             url = f"https://raw.githubusercontent.com/{USER}/miner/main/{FILE}.json"
             output_filename = "set-miner/online.json"
             response = requests.get (url, stream=True)
             response.raise_for_status() 
     with open(filename, 'wb') as f:
         for chunk in response.iter_content(chunk_size=8192):
             f.write(chunk)
             print(f"\n\033[93m{url}\033[0m\n")
             print("\033[1;33;40m")
             os.system("figlet -f ANSI_Shadow OK")
             print("\033[00m\n")

 except requests.exceptions.RequestException as e:
             print ("\n\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m\n")
             time.sleep(10)
             os.system ("python3 connect.py")

with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             user = loads['user']
             file = loads['file']
             USER = f"{user}"
             FILE = f"{file}"
url_to_download = f"https://raw.githubusercontent.com/{USER}/miner/main/{FILE}.json"
output_filename = "set-miner/online.json"
autoconnect(url_to_download, output_filename)