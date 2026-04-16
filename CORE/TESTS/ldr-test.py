print("A")

import shutil

print("B")

total, used, free = shutil.disk_usage(".")

print("C")

print(total, used, free)
