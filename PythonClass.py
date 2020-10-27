class Laptop:
    def feature1(self):
     print("Playing a YouTube video")
    
    def feature2(self):
     print("Studying for a big test")


class PC:
    def feature3(self):
     print("Playing a MMO videogame")
    
    def feature4(self):
     print("Designing a website")

class Smartphone(Laptop,PC):
    def feature5(self):
     print("Taking a zoom call")

    def feature6(self):
     print("Playing an app game")

Laptop = Laptop()

PC = PC()

Smartphone = Smartphone()

Smartphone.feature4()
Smartphone.feature1()




 



