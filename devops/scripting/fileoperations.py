with open("spider.txt") as file:
    print(file.readline().strip())
    mylist=print(file.readlines())

file = open("spider.txt")
for line in file:
    print(line.strip().upper())
file.close()


file = open("spider.txt")
lines = file.readlines()
file.close()

lines.sort()
print(lines)


with open("novel.txt","w") as file:
    file.write("It was a dark and stirmy night")


#################################################

guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("guests.txt") as guests:
    for line in guests:
        print(line)

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

with open("guests.txt") as guests:
    for line in guests:
        print(line)

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))

import os
import datetime
os.rename("novel.txt","mynov.txt")
os.remove("mynov.txt")
print(os.path.exists("mynov.txt"))

print(os.path.getsize("spider.txt")) #size of the file
timestamp = os.path.getmtime("spider.txt") #last modified time  it returns timestamp which needs to be converted to datetime using datetime module
print(datetime.datetime.fromtimestamp(timestamp))

print(os.path.abspath("spider.txt"))  # finds the absolute path

print(os.getcwd())  # gets the current working directory
#os.mkdir("new_dir") # creates a new directory
#os.chdir("new_dir") # changes to the new directory
print(os.getcwd())
#os.chdir("devops")
#os.rmdir("new_dir")
#os.getcwd()
print(os.listdir("venv"))

dir="venv"
for name in os.listdir(dir):
    ###nos.path.join function is independent acrross multiple paltforms. it adds "/" or "\" based on os
    fullname=os.path.join(dir,name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))





file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")

import os

"""
The create_python_script function creates a new python script in the current working directory, 
adds the line of comments to it declared by the 'comments' variable, and returns the size of the new file. 
Fill in the gaps to create a script called "program.py".
"""

def create_python_script(filename):
    comments = "# Start of a new Python program"
    with open(filename, "w") as file:
        file.write(comments)

    filesize = os.path.getsize(filename)

    return (filesize)


print(create_python_script("program.py"))


