
# Write a function oxford_comma() in the lib/oxford_comma.py file that takes an array of string elements as an argument and converts it into a string using the Oxford comma. 

def oxford_comma(items):
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    if len(items) > 2:
        return ', '.join(items)
    else:
        return ' '.join(items)