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