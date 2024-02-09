test_1 = ['codewars', 'flick', 'code', 'wars']
test_2 = ['flick', 'chocolate', 'adventure', 'sunshine']
test_3 = ['john, smith, susan', 'flick']

# def flick_switch(lst):
#     arr = []
#     value = True
#     for i in lst:
#         if i == 'flick':
#             value = not value
#         arr.append(value)
#     return arr


# print(flick_switch(test_2))

def flick_switch(lst):
    flick = True
    return [ (flick := flick ^ (v=='flick')) for v in lst]


# ok in the experession above the walrus symbol allows us to assign a value in an expression := and the carrot symbol ^ will return True only if one side of the evaluation is true if both sides are true it will return False this is not as the XOR operation exclusive operator 

# so in the function above as the list comprehension runs to fill the array every v element will check the condition in the condition we check if v == 'flick' since the starting value of flick is true if v == 'flick' is true the comparison will look like this true ^ true and since xor only returns true if one side is true this will return false then the walrus operator is used to assign the new value of flick to false and that value will be inserted into the array. now the next time it sees flick in the array it will try to compare again and get this false ^ true only one side is true so it returns true and assigns flick to true and adds the new value.