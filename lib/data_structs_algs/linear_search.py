
def linear_search(arr, num):
    for index, number in enumerate(arr):
        if number == num:
            return index
    return -1
