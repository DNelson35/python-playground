# def cat_mouse(x,j):
#     for i in range(len(x)):
#         if x[i] == 'C':
#             for k in range(i + j):
#                 if x[i + k] == 'D' or x[i - k] == 'D':
#                     return "Protected!"
#                 elif x[i + k] == 'm' or x[i - k] == 'm':
#                     return "Caught!"
#             print("Escaped!")
    
#     print('boring without all three')
        

# cat_mouse('...m....D....C.......', 5)
def cat_mouse_game(x, j): # failed attempt test case calls for an unexpected behavior that contradicts another test case i would have to through a specific exemtption for that case so it dosnt contradict the other rule 
    try:
        cat_pos = x.index('C')
        mouse_pos = x.index('m')
        dog_pos = x.index('D')
    except ValueError:
        return 'boring without all three'

    if abs(cat_pos - mouse_pos) <= j:
        if dog_pos >= min(cat_pos, mouse_pos) and dog_pos <= max(cat_pos, mouse_pos):
            return 'Protected!'
        else:
            return 'Caught!'
    else:
        return 'Escaped!'

