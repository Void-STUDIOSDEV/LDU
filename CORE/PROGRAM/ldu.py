import shutil
import time
import sys
import os
sleep = time.sleep
home = os.path.expanduser("~")
files = []

def disk_size():
		sleep(0.7); print("LISTING...")
		total, used, free = shutil.disk_usage(".")
		sleep(0.5); print("TOTAL: ", total / (1024**3), "GB")
		sleep(0.5); print("USED: ", used / (1024**3), "GB")
		sleep(0.5); print("FREE: ", free / (1024**3), "GB\n")
def file_list():
		sleep(0.5); print("\nLISTING...\n\n")
		for root, _, fs in os.walk(home):
			for f in fs:
				p = os.path.join(root, f)
				try:
					s = os.path.getsize(p)
					files.append((s, p))
				except:
					pass
			
		files.sort(reverse=True)
	
		for s, p in files[:5]:
			sleep(1); print(round(s/1024**3, 2), "GB", p) #adjust the sleep time, files will either appear faster or slower
#required modules, variables, and defs


sleep(0.5); print("\nLinux Disk Utilities, LDU")
sleep(0.5); print("Version 01.00.00")
sleep(0.5); print("COPYRIGHT VOID STUDIOS 2026")
sleep(0.5); print("COVERED UNDER GNU General Public License 2.x\n")
sleep(0.8); print("[E]XIT: Stops the program [does not auto-exit]")
sleep(0.5); print("[D]ISK: Shows storage capabilities [Total, Free, Used]")
sleep(0.5); print("[R]EAD: Lists largest files in HOME [~] directory")
sleep(0.5); print("<>E: Adding 'E' to any selection does an auto-stop after it runs.")
#introduction


while True:
	choice = input("SELECTION: ").upper()
	if choice == "E":
		sleep(0.5); print("Goodbye!")
		sleep(0.4); print(".")
		sleep(0.3); print("..")
		sleep(0.2); print("...")
		sleep(0.1); print("....")
		sleep(0.0); print(".....")
		break
	#this part allows users to exit, allowing safe exiting
	
	if choice == "D":
		disk_size()
		break
		
	if choice == "R":
		file_list()
		break
			
	if choice == "DE":
		disk_size()
		
	if choice == "RE":
		file_list()
		
	if choice not in ["D", "R", "DE", "RE"]:
		print("INVALID SELECTION\n")
