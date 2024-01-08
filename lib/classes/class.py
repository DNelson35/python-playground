class Dog:
    
    def bark(self):
        print("Woof!")

    def sit(self):
        print("The dog is sitting")


class Person:

    def talk(self):
        print("Hello world!")
    
    def walk(self):
        print("the person is walking")
        

fido = Dog()
damien = Person()

print(fido.bark())
print(fido.sit())
print(damien.talk())
print(damien.walk())

