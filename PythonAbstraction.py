from abc import ABC, abstractmethod 
class Computer(ABC):
    def memory(self, amount):
        print("memory amount:", amount)
        

    @abstractmethod
    def process(self):
        pass
        

class Laptop(Computer):
    def process(self, amount):
        print('your memory amount {} exceeds your 100% limit'.format(amount))

obj = Laptop()
obj.memory("120%")
obj.process("120%")
    


