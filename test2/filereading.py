"""

f=open("my_file.txt","w")
f.write("This is my second line")
f.close()

"""
"""
files=[]
for i in range(10000):
    files.append(open("some_file.txt","r"))
    print(i)


with (open("my_file.txt","r")) as f:
    for line in f:
        print(line)


with (open("my_file.txt","r")) as f:
    print(f.readlines())

"""


def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open(filename, "r") as f:
        for line in f:
            cast_list.append(line.split(',')[0])

    # use the for loop syntax to process each line
    # and add the actor name to cast_list

    return cast_list


cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)