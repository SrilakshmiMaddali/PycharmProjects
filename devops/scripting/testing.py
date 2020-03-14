#!/usr/bin/env python3
"""
import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = np.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())
"""

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename,"w") as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))

"""
The new_directory function creates a new directory inside the current working directory, 
then creates a new empty file inside the new directory, and returns the list of files in that directory. 
Complete the function to create a file "script.py" in the directory "PythonPrograms".


"""


import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
    if  not os.path.exists(directory):
      os.mkdir(directory)
    os.chdir(directory)
    with open(filename,"a") as file:
        pass
    return os.listdir(os.getcwd())
  # Create the new file inside of the new directory

  # Return the list of files in the new directory

print(new_directory("PythonPrograms", "script.py"))


########################################################

#!/usr/bin/env python3

#Import libraries

import csv
import re


def contains_domain(address, domain):
  """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
  domain_pattern=r"[\w\.-]+@"+domain+'$'
  if re.match(domain_pattern,address):
    return True
  return False

def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in
    the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern,new_domain,address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
  old_domain,new_domain = 'abc.edu','xyz.edu'
  csv_file_location='/home/student-04-5ee678140186/data/user_emails.csv'
  report_file = "/home/student-04-5ee678140186/data"+'/updated_user_emails.csv'
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []
  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address, old_domain, new_domain)
        new_domain_email_list.append(replaced_email)
    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    for user in user_data_list[1:]:
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
  f.close()
  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    output_file.close()
main()

"""
Full Name, Email Address
Blossom Gill, blossom@xyz.edu
Hayes Delgado, nonummy@utnisia.com
Petra Jones, ac@xyz.edu
Oleg Noel, noel@liberomauris.ca
Ahmed Miller, ahmed.miller@nequenonquam.co.uk
Macaulay Douglas, mdouglas@xyz.edu
Aurora Grant, enim.non@xyz.edu
Madison Mcintosh, mcintosh@nisiaenean.net
Montana Powell, montanap@semmagna.org
Rogan Robinson, rr.robinson@xyz.edu
Simon Rivera, sri@xyz.edu
Benedict Pacheco, bpacheco@xyz.edu
Maisie Hendrix, mai.hendrix@xyz.edu
Xaviera Gould, xlg@utnisia.net
Oren Rollins, oren@semmagna.com
Flavia Santiago, flavia@utnisia.net
Jackson Owens, jackowens@xyz.edu
Britanni Humphrey, britanni@ut.net
Kirk Nixon, kirknixon@xyz.edu
Bree Campbell, breee@utnisia.net
"""