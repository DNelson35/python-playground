# def is_valid_walk(walk): initial code without rewrite
#     directions = {'n': 1, 's': -1, 'e': 1, 'w': -1}
#     x = 0
#     y = 0
#     if len(walk) != 10:
#         return False

#     for i in walk:
#         if i in directions:
#             if i == 'n' or i == 's':
#                 y = directions[i] + y
#             else:
#                 x = directions[i] + x

#     return True if x == 0 and y == 0 else False

# finished code

def is_valid_walk(walk):
    directions = {'n': (0,  1), 's': (0, -1), 'e': (1,  0), 'w': (-1,  0)}
    x, y =  0,  0

    if len(walk) != 10:
        return False
    
    for direction in walk:
        dx, dy = directions.get(direction, (0, 0))
        x += dx
        y += dy

    return x == 0 and y == 0
    

