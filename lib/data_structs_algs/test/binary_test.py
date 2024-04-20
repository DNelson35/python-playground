#!/usr/bin/env python3

import sys
import importlib
import os
import time


if len(sys.argv) < 2:
    print('Please provide the file name of the module to test.')
    sys.exit(1)


# get the current scripts directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# get the parent directory of the test folder one level up
parent_dir = os.path.dirname(current_dir)

# add the parent directory to the system path
sys.path.append(parent_dir)

module_name = sys.argv[1].replace('.py', '')


module = importlib.import_module(module_name)



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

# large test
tests.append({
    'input': {
        'arr': list(range(10000000, 0, -1)),
        'num': 2
    },
    'output': 9999998
})


for index, test in enumerate(tests):

    start_time = time.time()
    if module_name == 'binary_search':
        result = module.locate_num(**test['input'])
    else:
        result = module.linear_search(**test['input'])

    if result == test['output']:
        print(f"\033[92mPass on test {index}\nexpected {test['output']} got {result}\ntime: {(time.time() - start_time) * 1000:.4f}m \n\033[0m")
    else:
        print(f"\033[91mFailure in test {index}\n{tests[index]}\nactual {result} != expected {test['output']}\033[0m")

