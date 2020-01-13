##################
"""
age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
"""
######################################

print(type("Hey".replace("ey","i")[-1]))
print("Hey".replace("ey","i"))

###############
d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

print(d["employees"][1]["lastName"])
d["employees"][1]["lastName"]="Smooth"
print(d["employees"][1]["lastName"])
d["employees"].append(dict(firstName="Albert",lastName="Bert"))
print(d)
