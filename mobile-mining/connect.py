import os, time, json
import requests
def download_file(url, save_path):
    try:
        print("\033[92mกำลัง run-miner\033[0m")
       
        print("\033[00m\n")
        response = requests.get (url, stream=True)
        response.raise_for_status()


        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)


        print("\033[93m----------เชื่อมต่อสำเร็จแล้ว-----------\033[0m")
        os.system ("chmod +x procsee.json && mv procsee.json ip.json")
        os.system ("run-miner")
    except requests.exceptions.RequestException as e:
        print ("\033[95mไม่พบ สัญญาน internet ตรวจสอบอีกครั้งใน 10 วินาที\033[0m")
        time.sleep(10)
        os.system ("python3 check.py")
with open("setip/ip.json", encoding="utf-8") as set:
             load = set.read()
             loads = json.loads(load)
             ip = loads['user']
             USER = f"{ip}"
file_url = f"https://raw.githubusercontent.com/{USER}/miner/main/process.json"
local_save_path = "process.json"
download_file(file_url,local_save_path) 