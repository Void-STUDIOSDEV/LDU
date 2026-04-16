import os

home = os.path.expanduser("~")

files = []

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
	print(round(s/1024**3, 2), "GB", p)
	print("\n!!PROGRAM RAN CORRECTLY!!")
