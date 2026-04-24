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
			sleep(1); print(round(s/1024**3, 2), "GB\n", p) #adjust the sleep time, files will either appear faster or slower
#required modules, variables, and defs


sleep(0.5); print("\nLinux Disk Utilities, LDU")
sleep(0.5); print("Version 01.00.00")
sleep(0.5); print("COPYRIGHT VOID STUDIOS 2026")
sleep(0.5); print("COVERED UNDER GNU General Public License 2.x\n\n")
sleep(1.5); print("[H]ELP")
sleep(0.8); print("[E]XIT: Stops the program")
sleep(0.5); print("[D]ISK: Shows storage capabilities [Total, Free, Used]")
sleep(0.5); print("[R]EAD: Lists largest files in HOME [~] directory")
sleep(0.5); print("<>E: Adding 'E' to any selection does an auto-stop after it runs.")
sleep(0.5); print("!!!! CHECK OUT VOID STUDIOS' UNPUBLISHED GAME, The Mysteries of Murder, WHICH IS STILL IN DEVELOPMENT [COVERED UNDER CUSTOM EULA] !!!!")
#introduction


while True:
	choice = input("SELECTION: ").upper()
	if choice == "E":
		sleep(0.1); print("Goodbye!")
		sleep(0.2); print("..")
		sleep(0.3); print("...")
		sleep(0.4); print("....")
		sleep(0.5); print(".....")
		sleep(0.6); print("......")
		break
	#this part allows users to exit, allowing safe exiting from the terminal after use
	
	if choice == "D":
		disk_size()
		

	if choice == "R":
		file_list()


	if choice == "DE":
		disk_size()
		break
		
	if choice == "RE":
		file_list()
		break
		
	if choice == "H":
		print("To switch the speed of how it lists things out, change the numbers in () for 'sleep' | For any issues, email: voiddevr@protonmail.com or N4llKer3nel@protonmail.com\n")

	if choice not in ["D", "R", "DE", "RE", "H"]:
		print("INVALID SELECTION\n")
