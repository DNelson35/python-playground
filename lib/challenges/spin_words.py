def spin_words(string):
    return ' '.join([word[::-1] if len(word) >=  5 else word for word in string.split(' ')])

print(spin_words("this should be called somthing better"))


