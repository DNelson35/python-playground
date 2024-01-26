def pyramid_rightmost_numbers(n):
    rightmost_numbers = []
    step = 0
    i = 1
    while i <= n:
        rightmost_number = i + step
        i = rightmost_number + 1
        step += 1
        rightmost_numbers.append(rightmost_number)
    
    return rightmost_numbers

def decode(message_file): 
    with open(message_file) as f:
        lines_obj = {}
        length = 0
        steps = 0
        for line in f:
            if line != '\n':
                line_arr = line.strip('\n').split(' ')
                lines_obj[line_arr[0]] = line_arr[1]
                length += 1

    numbers = pyramid_rightmost_numbers(length)

    solution = []

    for i in numbers:
        solution.append(lines_obj[f"{i}"])

    return ' '.join(solution)


print(decode('lib/data/decoding_data.txt'))

# Solution: opposite sun rain think ocean to winter wild it ready buy card possible would electric stay post paragraph produce state our compare touch possible