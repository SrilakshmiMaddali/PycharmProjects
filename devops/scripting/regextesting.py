import re
result = re.search(r"/(\w+)\_","/home/jane_contact")
print(result[1])

result =re.search(r"ticky: INFO: ([\w ]*) ", "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)")

user = re.search(r"\((.*)\)","May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)")

print(user[1])

print(result[1])