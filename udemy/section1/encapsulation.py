class Myclass:
    __hidden=0
    def add(self,increment):
        self.__hidden+=increment
        print(self.__hidden)


obj=Myclass()
obj.add(10)