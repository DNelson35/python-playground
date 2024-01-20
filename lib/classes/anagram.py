# code challenge figure out how to make a class that takes a string and finds an anagram with a match method
class Anagram:

    def __init__(self, word):
        self.word = sorted(char for char in word)
    
    def match(self, l):
        matching = []
        for word in l:
            if sorted([char for char in word]) == self.word:
                matching.append(word)
        
        print(matching)
        return matching
            

listen = Anagram("listen")
listen.match(["listen", "silent", "hippopotamus"])  
print("hello world")

# how to use a lambda function which is  really cool and
# obj = {  
#     "noodle": lambda n: n + 1
# }

# print(obj["noodle"](1))