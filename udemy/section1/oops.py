class Computer:
    def __init__(self,ram,processor,memory):
        self.ram=ram
        self.processor=processor
        self.memory=memory
    def getspecs(self):
        print("Enter the details")
        self.ram=input("Enter ram:")
        self.processor=input("Enter processor name:")
        self.memory=input("Enter memory:")



    def displayspecs(self):
        print("Ram: {}".format(self.ram))
        print("Memory: {}".format(self.memory))
        print("Processor: {}".format(self.processor))


class Laptop(Computer):
    def __init__(self,weight):
        self.weight=weight
    def getsweight(self):
        self.weight=input("Enter weight:")
    def displayweight(self):
        print("Laptop Weight:{}".format(self.weight))

class Desktop(Computer):
    def __init__(self,casecolor):
        self.casecolor=casecolor
    def getcasecolor(self):
        self.casecolor=input("Enter case color:")
    def displaycasecolor(self):
        print("Desktop case color is :{}".format(self.casecolor))

comp = Computer("","","")
comp.getspecs()

lappy=Laptop("")
lappy.getspecs()
lappy.getsweight()

desky=Desktop("")
desky.getspecs()
desky.displayspecs()
desky.getcasecolor()