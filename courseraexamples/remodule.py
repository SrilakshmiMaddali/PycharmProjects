####Regular expressions


import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)


txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)