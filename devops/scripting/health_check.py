import shutil
import psutil
from network import *

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = (du.free / du.used) * 100
    return free > 20


def check_cpu_usage():
    usage=psutil.cpu_percent(1)
    return usage<75


if not check_disk_usage("/") or not check_cpu_usage():
    print("Error!!")
elif check_localhost() and check_connectivity():
    print("Everything is OK!")
else:
    print("Network Failed")


with open("hello_world.txt") as text:
    for line in text:
	    print(line.strip())