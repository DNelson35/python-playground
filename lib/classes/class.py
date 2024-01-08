class Dog:
    def __init__(self, name="Mutt", breed="Mutt"):
        self.name = name
        self.breed = breed

    def sit(self):
        print(f"{self.name} is sitting down good dog")

    def ped(self):
        print(f"it is know that this {self.breed} is a good breed of pup")


class Person:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        if(self.name):
            print(f"Hi, my name is {self.name}")
        else:
            print(f"I have amnesia")
    


Damien = Person("Damien")

Damien.greet()

Everest = Dog("Everest")
Everest.sit()
Everest.ped()