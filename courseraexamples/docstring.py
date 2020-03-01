"""
A docstring is a brief text that explains what something does. 
Let's see how this works with a simple function.
 First off, we want to define the function. 
 So def, we'll call it to_seconds and we'll give it the parameters hours, minutes, and seconds. After that, we add our docstring.
  We do this by typing a string between triple quotes and we indent it to the right like the body of the function. 
  Returns the amount of seconds in the given hours, minutes, and seconds.
"""

def to_seconds(hours,minutes,seconds):
    """ Return the amount of seconds in the given hours,minutes and seconds"""
    return hours*3600+minutes*60+seconds

help(to_seconds)


class Person:
  def __init__(self, name):
    self.name = name
  def greeting(self):
    """Outputs a message with the name of the person"""
    print("Hello! My name is {name}.".format(name=self.name)) 

help(Person.greeting)


