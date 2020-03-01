import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename) as flowers_csv:
      reader=csv.DictReader(flowers_csv)
      for row in reader:
          return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))


####################################################################

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file
  create_file(filename)

  # Open the file
  with open(filename) as file:
    # Read the rows of the file
    rows = csv.reader(file)
    # Process each row
    next(rows,None)
    for row in rows:
        name,color,type= row
        return_string += "a {} {} is {}\n".format(name,color,type)
  return return_string

#Call the function
print(contents_of_file("flowers.csv"))

#############################################################################
"""
Convert employee data to dictionary

The goal of the script is to read the CSV file and generate a report with the total number of people in each department. 
To achieve this, we will divide the script into three functions.

Let's start with the first function: read_employees(). 
This function receives a CSV file as a parameter and returns a list of dictionaries from that file. 
For this, we will use the CSV module.

The CSV module uses classes to read and write tabular data in CSV format. 
The CSV library allows us to both read from and write to CSV files.
"""

# !/usr/bin/env python3

import csv

"""
Open the CSV file by calling open and then csv.DictReader.

DictReader creates an object that operates like a regular reader (an object that iterates over lines in the given CSV file), 
but also maps the information it reads into a dictionary where keys are given by the optional fieldnames parameter.
 If we omit the fieldnames parameter, the values in the first row of the CSV file will be used as the keys. 
 So, in this case, the first line of the CSV file has the keys and so there's no need to pass fieldnames as a parameter.

We also need to pass a dialect as a parameter to this function. There isn't a well-defined standard for comma-separated value files, 
so the parser needs to be flexible. Flexibility here means that there are many parameters to control how csv parses or writes data. 
Rather than passing each of these parameters to the reader and writer separately, we group them together conveniently into a dialect object.

Dialect classes can be registered by name so that callers of the CSV module don't need to 
know the parameter settings in advance. 
We will now register a dialect empDialect.
"""

def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect='empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list


employee_list = read_employees("employee.csv")
print(employee_list)
#'/home/student-03-1c4283d22ed1/data/employees.csv')


def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["Department"])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


dictionary = process_data(employee_list)
print(dictionary)


def write_report(dictionary, report_file):
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()


write_report(dictionary,'test_report.txt')
             #'/home/student-03-1c4283d22ed1/test_report.txt')

