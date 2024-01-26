def count_targets(n, sequence):
    total = 0
    for i in range(len(sequence)):
        if i >= n: 
            if sequence[i - n] == sequence[i]:
                total += 1
    return total


count_targets(2, [1,1,1,1,1,1])
    
