import csv
f = open("csvfile.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name,phone,role = row  # called as unpacking variables
    print("Name: {}, Phone: {}, Role: {} ".format(name,phone,role))
f.close()


#writing into csv files
hosts=[["Workstation.local","192.168.25.46"],["webserver.cloud","10.2.5.6"]]
with open("csv_writer.txt","w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

#Reading a dictionary
with open("software.csv") as dict_file:
    reader = csv.DictReader(dict_file)
    for row in reader:
        print(("{} has {} users").format(row["Name"],row["users"]))


#writing a dictionary into a csv file

users=[{"name":"Sol Mansi","username":"solm","department":"IT infrastructure"},
       {"name":"Lio Nelson","username":"lion","department":"User Experience Research"},
       {"name":"Charlie Grey","username":"greyc","department":"Development"}]
keys = ["name","username","department"]
with open("by_deparment.csv","w") as by_department:
    writer = csv.DictWriter(by_department,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
