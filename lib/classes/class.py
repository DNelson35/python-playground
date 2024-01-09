# for setting up a class learing how to initialize use setter getter methods as well as use self
class Dog:
    def __init__(self, name="Mutt", breed="Mutt"):
        self.name = name
        self.breed = breed

    def sit(self):
        print(f"{self.name} is sitting down good dog")

    def ped(self):
        print(f"it is know that this {self.breed} is a good breed of pup")
    
    def get_name(self):
        print(self._name)

    def set_name(self, name):
        if len(name) > 25 or type(name) != str:
            print("name must be less than 25 characters")
        else:
            self._name = name

    def get_breed(self):
        print(self._breed)

    def set_breed(self, breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
        if breed in approved_breeds:
            self._breed = breed
        else:
            print("not approved breed")

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

class Person:
    species = "Homo sapiens"
    def __init__(self, name, age, job="Admin"):
        self.name = name
        self.age = age
        self.job = job
    
    def greet(self):
        if(self.name):
            print(f"Hi, my name is {self.name}")
        else:
            print(f"I have amnesia")

    def get_age(self):
        print("Retrieving age.")
        return self._age

    def set_age(self, age):
        if (type(age) in (int, float)) and (0 <= age <= 120):
            print(f"Setting age to { age }.")
            self._age = age
        else:
            print("Age must be a number between 0 and 120.")

    def get_name(self):
        print(self._name)
    
    def set_name(self, name):
        if len(name) > 25 or type(name) != str:
            print("name must be shorter than 25 characters")
        else:
            self._name = name
    
    def get_job(self):
        print(self._job)
    
    def set_job(self, job):
        approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production", "Legal", "Finance", "Sales", "General Management", "Research & Development", "Marketing", "Purchasing"]
        
        if job in approved_jobs:
            self._job = job
        else:
            print("not an approved job")
    


    age = property(get_age, set_age)
    name = property(get_name, set_name)
    job = property(get_job, set_job)
    


Damien = Person("Damien", 30)
# Damien.age = 0
# Damien.age = False
# Damien.age = 66
# Damien.age

Damien.job
Damien.job = "steam engine"
Damien.job = "Legal"
Damien.job

Damien.name = "this is the song that never ends becuase im just in that type of mood or somthin"

Damien.name = "Damien Nelson"
Damien.name



# Everest = Dog("Everest", "Pug")
# Everest.name = "nelson"
# Everest.name
# Everest.breed
# Everest.breed = "Pointer"
# Everest.breed


