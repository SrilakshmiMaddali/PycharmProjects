import string
from math import pi

my_range=range(1,21)
"""count =0
for i in my_list:
    my_list[count]=i*10
    count+=1
"""


print([x*10 for x in my_range])



###################

my_range=range(1,21)
#print([str(x) for x in my_range])
print(list(map(str,my_range)))

#######################

a = ["1", 1, "1", 2]
b = set(a)
print(list(b))

######################

d = {"a": 1, "b": 2, "c": 3}
#sum=0
#for value in d.values():
#    sum+=value
print(sum(d.values()))


#######################
d = {"a": 1, "b": 2, "c": 3}
print(d["a"]+d["b"])

###################

d = {"a": 1, "b": 2}
d["c"]=3
print(d)

################### Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
d = dict((key,value) for key,value in d.items() if value<=1)
print(d)

###################
d = {"a":list(range(1,11)),"b":list(range(11,21)),"c":list(range(21,31))}
print(d)

print(d["b"][2])

#print("b has value {} ".format( d["b"]))
#print("c has value {} ".format( d["c"]))
#print("a has value {} ".format( d["a"]))

for key,value in d.items():
    print(key," has value ",value)

############################

#Make a script that prints out letters of English alphabet from a to z, one letter per line in the terminal.
for letter in string.ascii_lowercase:
    print(letter)

###############################

for x in range(1,11):
    print(x)

#print(x for x in range(1,11)) generates generator object error

###############

def accelarator(v1,v2,t1,t2):
    result=(v2-v1)/(t2-t1)
    return result

print(accelarator(0,10,0,20))

##################volume calculator

def spherevolume(h,r=10):
    sol = ((4*pi*r**3)/3)-((pi*h**2*(3*r-h))/3)
    return sol
print(spherevolume(2))

##################### error correction

def foo(a=1, b=2):
    return a + b

x = foo() - 1
print(x)

################## global variable
c = 1
def foo():
    return c
c = 3
print(foo())

#################global variable scope

c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

##################Create a function that takes any string as input and returns the number of words for that string.

def foo(mystr):
    my_list=mystr.split(" ")
    return len(my_list)

print(foo("This is my list hi"))

##################create a Python function that takes a text file as input and returns the number of words contained in the text file.

def foo(filepath):
    with open(filepath,"r") as file:
        mystr=file.read()
        mylist=mystr.split(" ")
        return len(mylist)


print(foo("words1.txt"))

##############Create a function that takes a text file as input and returns the number of words contained in the text file. Please take into consideration that some words can be separated by a comma with no space.

def foo(filepath):
    with open(filepath) as file:
        mystr=file.read()
        mystr=mystr.replace(",", " ")
        mylist=mystr.split(" ")
        return len(mylist)

print(foo("words2.txt"))

################fixing cosine
import math
math.cos(1)

#################fixing error
import math
print(math.pow(2,3))

###################writing letters onto a textfile

def foo(filepath):
    with open(filepath,"w") as file:
        for letter in string.ascii_lowercase:
            file.write(letter + "\n")


####################Print out in each line the sum of homologous items of the two sequences.

a = [1, 2, 3]
b = (4, 5, 6)

for i,j in zip(a,b):
    print(i+j)

#####################Create a script that generates a file where all letters of English alphabet are listed two in each line.
def foo(filepath):
    with open(filepath,"w") as myfile:
        for letter1,letter2 in zip(string.ascii_lowercase[0::2],strng.ascii_lowercase[1::2]):
            myfile.write(letter1+letter2+"\n")


##################
def foo(filepath):
    with open(filepath,"w") as myfile:
        for letter1,letter2,letter3 in zip(string.ascii_lowercase[0::3],string.ascii_lowercase[1::3],string.ascii_lowercase[2::3]):
            myfile.write(letter1+letter2+letter3+"\n")

foo("letters.txt")

############## create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt.
import os
if not os.path.exists("letters"):
    os.makedirs("letters")
def foo():
    for letter in string.ascii_lowercase:        
        with open("letters/"+letter+".txt","w") as file:
            file.write(letter+"\n")
foo()
