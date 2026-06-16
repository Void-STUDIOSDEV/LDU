import shutil
import sys
import os
import time
import platform
import time
current_os = platform.system()
files = []

def progWindows():
		home = os.path.expanduser("C:\\")
		time.sleep(0.7); print("LISTING...\n")
		total, used, free = shutil.disk_usage(".")
		time.sleep(0.5); print("TOTAL: ", total / (1024**3), "GB")
		time.sleep(0.5); print("USED: ", used / (1024**3), "GB")
		time.sleep(0.5); print("FREE: ", free / (1024**3), "GB\n")

		home = os.path.expanduser("C:")
		time.sleep(0.5); print("LISTING...\n\n")
		for root, _, fs in os.walk(home):
			for f in fs:
				p = os.path.join(root, f)
				try:
					s = os.path.getsize(p)
					files.append((s, p))
				except:
					pass
			
		files.sort(reverse=True)
	
		for s, p in files[:7]:
			time.sleep(0.5); print(round(s/1024**3, 2), "GB\n", p) #adjust the sleep time, files will either appear faster or slower
#required modules, variables, and defs


def progLinux():
		home = os.path.expanduser("~/")
		time.sleep(0.7); print("LISTING...\n")
		total, used, free = shutil.disk_usage(".")
		time.sleep(0.5); print("TOTAL: ", total / (1024**3), "GB")
		time.sleep(0.5); print("USED: ", used / (1024**3), "GB")
		time.sleep(0.5); print("FREE: ", free / (1024**3), "GB\n")

		home = os.path.expanduser("~/")
		time.sleep(0.5); print("LISTING...\n\n")
		for root, _, fs in os.walk(home):
			for f in fs:
				p = os.path.join(root, f)
				try:
					s = os.path.getsize(p)
					files.append((s, p))
				except:
					pass
			
		files.sort(reverse=True)
	
		for s, p in files[:7]:
			time.sleep(0.5); print(round(s/1024**3, 2), "GB\n", p) #adjust the sleep time, files will either appear faster or slower
#required modules, variables, and defs



if current_os == "Windows":
	print("WINDOWS MACHINE DETECTED. FUNCTION IS 100%")
	progWindows()

if current_os == "Linux":
	print("LINUX MACHINE DETECTED. FUNCTION IS 100%")
	progLinux()
