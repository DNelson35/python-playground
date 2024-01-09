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