from abc import ABC, abstractmethod 
class Computer(ABC):

    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print("its running")
        
class Whiteboard(Computer):
    def write(self):
        print("its writing")
        
        

obj = Whiteboard()
obj.process("writing")
obj.Laptop("running")








