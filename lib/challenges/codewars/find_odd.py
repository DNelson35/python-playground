# since in this case there will only be one i could have just returned the only i in seq that evalueates to true in the condition but in the case there is more than one all odd numbered occurrences will be pushed to the array
def find_it(seq): 
    arr = []

    for i in seq:
        if seq.count(i) % 2 == 1: arr.append(i)
    
    return list(set(arr))[0]



