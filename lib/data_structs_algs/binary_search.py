import math
# common test
test_arr = [13,11,12,7,4,3,1,0]
tests = []

# test if number is middle of array
tests.append({
    'input': {
        'arr': test_arr,
        'num': 7
    },
    'output': 3
})

# test if number is towards the end of array
tests.append({
    'input': {
        'arr': test_arr,
        'num': 1
    },
    'output': 6
})

# test if number is first element in array
tests.append({
    'input': {
        'arr': [4,2,1,-1],
        'num': 4
    },
    'output': 0
})

#test if number is last element in array
tests.append({
    'input': {
        'arr': [3,-1,-9,-127],
        'num': -127
    },
    'output': 3
})

#test if array only has one element
tests.append({
    'input': {
        'arr': [6],
        'num': 6
    },
    'output': 0
})

# test if number doesn't exist in array
tests.append({
    'input': {
        'arr': [9,7,5,2,-9],
        'num': 4
    },
    'output': -1
})

#test array is empty
tests.append({
    'input': {
        'arr': [],
        'num': 7
    },
    'output': -1
})

# numbers can repeat in cards
tests.append({
    'input': {
        'arr': [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'num': 3
    },
    'output': 7
})

# our search number can repeat
tests.append({
    'input': {
        'arr': [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'num': 6
    },
    'output': 2
})

def test_location(arr, num, mid):
    mid_number = arr[mid]
    print('mid:', mid, ", mid_number:", mid_number)
    if mid_number == num:
        if mid-1 >= 0 and arr[mid-1] == num:
            return 'left'
        else:
            return 'found'
    elif mid_number < num:
        return 'left'
    else:
        return 'right'


def binary_search(arr, num):
    lo, hi = 0, len(arr) - 1

    
    while lo <= hi:
        print('lo:', lo, 'hi:', hi)
        mid = (lo + hi) // 2
        result = test_location(arr, num, mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid -1
        elif result == 'right':
            lo = mid + 1
        
    return -1


for index, test in enumerate(tests):
    result = binary_search(**test['input'])
    if result == test['output']:
        print(f"\033[92mPass on test {index}\nexpected {test['output']} got {result}\n\033[0m")
    else:
        print(f"\033[91mFailure in test {index}\n{tests[index]}\nactual {result} != expected {test['output']}\n\033[0m")

    

  
    




    
