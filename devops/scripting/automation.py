#to find out disk storage space we use shutil module


import shutil
import psutil
ds=shutil.disk_usage("/")
print(ds)
print(ds.free/ds.used*100)


#to find out cpu usage we use psutil

print(psutil.cpu_percent(0.1))







