import shutil
import sys

def check_disk_usage(disk,min_absolute,min_percent):
    """Returns True if there is enough free disk space, false otherwise """
    du = shutil.disk_usage(disk)
    #calculate percentage of free space
    percent_free = 100 * du.free / du.total
    #calculate how many free giga bytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

if not check_disk_usage("/",2*2**30,10):
    print("ERROR: Not enough disk space")
    return 1

print("Everything OK")
return 0