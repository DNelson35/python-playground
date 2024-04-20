import math

# second write
def test_location(arr, num, mid):
    if arr[mid] == num:
        if mid-1 >= 0 and arr[mid-1] == num:
            return 'left'
        else:
            return 'found'
    elif arr[mid] < num:
        return 'left'
    else:
        return 'right'

# first write
# def test_location(arr, num, mid):
#     mid_number = arr[mid]
#     print('mid:', mid, ", mid_number:", mid_number)
#     if mid_number == num:
#         if mid-1 >= 0 and arr[mid-1] == num:
#             return 'left'
#         else:
#             return 'found'
#     elif mid_number < num:
#         return 'left'
#     else:
#         return 'right'

def binary_search(arr, num): # O(log n)
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(arr, num, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1   
    return -1



    

  
    




    
