# AUTO RUN CCMINER IN TERMUX

* แตะจอค้าง เลือก more
* เลือก Keep screen on

```
termux-setup-storage
```
* กดยอมรับ

```
pkg update -y
```
พิมพ์ N ในทุกการเรียกถาม
```
pkg install proot-distro -y && proot-distro install ubuntu && pkg install nano -y && pkg install wget -y && cd /data/data/com.termux/files/usr/etc && nano profile
```
* เลื่อนเคอร์เซอร์ลงไปล่างสุด ในบรรทัดสุดท้าย ใส่คำสั่ง
```
proot-distro login ubuntu
```
* ctrl+x แล้วตอบ y เพื่อ save
* ปิด แล้วเปิด termux ใหม่อีกครั้ง

## การติดตั้งตามขั้นตอน
```
apt-get update -y && apt-get install git -y && git clone https://github.com/saengx/CCMINER-SERVER && cd CCMINER-SERVER && chmod +x setup.sh && sh setup.sh
```
* หลังจากเปิดไฟล์ bash.bashrc เพิ่มบรรทัดแรกด้วยการ enter เลื่อนเคอร์เซอร์ขึ้นด้านบน ใส่คำสั่ง
- ```run-miner```
* แล้ว ctrl+x ตอบ y เพื่อ save

# เพิ่มเติมการใช้โปรแกรม

## กรณีหากเป็น zergpool การใส่password ไม่ต้องใส่ ID=ชื่อ ระบบจะทำการaddใส่ให้อัตโนมัติ
* หากต้องการหยุดขุดให้ใช้กด ```CTRL + C```
* หากต้องการเปลี่ยน TAG ใช้คำสั่ง ```edit-miner```
* หากต้องการเปิดขุด ใช้คำสั่ง ```run-miner```

* หากต้องการเพิ่ม ip สำหรับเชื่อมต่อ ใช้คำสั่ง ```add-ip```
# AUTORUN-CCMINER-X
