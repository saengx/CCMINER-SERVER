import os, time, json
from config import banneredit
from multiprocessing import cpu_count


cpu_thread = cpu_count()


def OffMiner():
  
   banneredit()
   try:
       print("ตัวอย่าง:")
       print(" \033[93mstratum+tcp://ap.luckpool.net:3956\033[00m")
       print(" \033[93mstratum+tcp://sg.vipor.net:5040\033[00m")
       pool = input(" pool : ")
       print("\033[35m-----------------------------------------\033[0m")
        
       print("ตัวอย่าง: \033[93mRJMw1DQJeNGJUfhYxZa5hx1gtfpRPySiXW\033[00m")
       wallet = input("wallet: ")
       print("\033[35m-----------------------------------------\033[0m")

       print("ตัวอย่าง:")
       print("  \033[93mx หรือ ( hybrid เฉพาะ luckpool )\033[00m")
       print("  \033[93mc=DOGE,mc=VRSC (ไม่ต้องใส่ id=ชื่อ ระบบจะเพิ่มให้เอง)\033[00m")
       password = input("password : ")
       print("\033[35m-----------------------------------------\033[0m")

       if pool == "" or wallet == "":
          raise Exception()
       if password == "":
          raise Exception()
   except:
            os.system("@cls||clear")
            print("เกิดข้อผิดพลาดโปรดตั้งค่าใหม่!")
            time.sleep(3)
            os.system("edit-miner")   
   push = {
         'pool': pool,
         'wallet': wallet,
         'pass': password
          }
   with open("set-miner/online.json", "w") as set:
        json.dump(push, set, indent=4)

        print("ชื่อคนงานขุด เช่น \033[93mMiner01\033[00m")
        name = input("[-n]: ")
        print("\033[35m-----------------------------------------\033[0m")
        
        print(f"จำนวนthread \033[93mค่าที่ใส่ได้คือ 0 ถึง {cpu_thread}\033[00m")
        cpu = int(input("[-t]: "))
        print("\033[35m-----------------------------------------\033[0m")
        
        if name == "":
            name = "x"
        if cpu == "":
            cpu = 1
        
        push = {
                 'name': name,
                 'cpu': cpu
               }
        with open("set-miner/offline.json", "w") as set:
             json.dump(push, set, indent=4)
             
while True:
  banneredit()
  OffMiner()
  os.system("run-miner")     
  break
