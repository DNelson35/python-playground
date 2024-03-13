def solution(s):
    if(s == ''): return []
    string_arr = [s[i:i+2] for i in range(0, len(s), 2)]

    if(len(string_arr[-1]) == 1):
        string_arr[-1] += '_'
    
    return string_arr


