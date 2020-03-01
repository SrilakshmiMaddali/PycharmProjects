class Apple:
    color=""
    flavor=""
    

fuji=Apple()
fuji.color="Red"
fuji.flavor="sweet"

print(fuji.flavor)


class Piglet:
    name="Piglet"
    def speak(self):
        print("Oink!I am {} Oink!".format(self.name))

hamlet=Piglet()
hamlet.name="Hamlet"
hamlet.speak()

class Dog:
  years = 0
  def dog_years(self):
    return self.years*7
    
fido=Dog()
fido.years=3
print(fido.dog_years())

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name) 

# Create a new instance with a name of your choice
some_person = Person("Sri")  
# Call the greeting method
print(some_person.greeting())

class Myapple:
    def __init__(self,color,flavor):
        self.color=color
        self.flavor=flavor
    def __str__(self):
        return "This Apple is {} in color and {}".format(self.color,self.flavor)

jonagold=Myapple("red","sweet")
print(jonagold)


class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom=bottom
        self.top=top
        self.current=current
    def __str__(self):
        return "Current floor:{}".format(self.current) 
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current<self.top:
            self.current+=1
        
            
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current>self.bottom:
            self.current-=1
        
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current=floor

elevator = Elevator(-1, 10, 0)

elevator.up() 
elevator.current #should output 1
elevator.down() 
elevator.current #should output 0
elevator.go_to(10) 
elevator.current #should output 10
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1
elevator.go_to(5)
print(elevator)
