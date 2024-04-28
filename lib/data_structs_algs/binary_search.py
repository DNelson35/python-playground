import math

# second write 
# def test_location(arr, num, mid):
#     if arr[mid] == num:
#         if mid-1 >= 0 and arr[mid-1] == num:
#             return 'left'
#         else:
#             return 'found'
#     elif arr[mid] < num:
#         return 'left'
#     else:
#         return 'right'


# def binary_search(arr, num): # O(log n)
#     lo, hi = 0, len(arr) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         result = test_location(arr, num, mid)
#         if result == 'found':
#             return mid
#         elif result == 'left':
#             hi = mid -1
#         elif result == 'right':
#             lo = mid + 1   
#     return -1

# third write

def binary_search(lo, hi, condition):
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def locate_num(arr, num):
    def condition(mid):
        if arr[mid] == num:
            if mid > 0 and arr[mid - 1] == num:
                return 'left'
            else:
                return 'found'
        elif arr[mid] < num:
            return 'left'
        else:
            return 'right'

    return binary_search(0, len(arr) - 1, condition)



def find_rotations(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid < high and arr[mid] > arr[mid + 1]:
            return mid + 1
        elif mid > 0 and arr[mid] < arr[mid - 1]:
            return mid
        elif arr[low] >= arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return 0

# Example usage
arr = [7, 8, 9, 10, 1, 2, 3]
print(find_rotations(arr)) # Output: 6