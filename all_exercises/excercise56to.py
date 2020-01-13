import json
from pprint import pprint

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

with open("Company2.json","w") as outfile:
    json.dump(d,outfile,indent=4)


#####################Json to dictionary
with open("Company2.json","r") as file:
    data=json.loads(file.read())

pprint(data)

######################update Json
with open("Company2.json","r+") as file:
    data=json.loads(file.read())
    data["employees"].append(dict(firstName="Albert",lastName="Bert"))
    file.seek(0)
    json.dump(data,file,indent=4,sort_keys=True)
    file.truncate()

#######################
a = [1, 2, 3]
for index,i in enumerate(a):
    print("Item %s has index %s" %(i,index))
######################
"""
import time
i=0
while True:
    i+=1
    print("Hello")
    time.sleep(i)
"""

##################
import time
i=0
while True:
    i+=1
    print("Hello")

    if i>3:
        print("End of loop")
        break
    time.sleep(i)
