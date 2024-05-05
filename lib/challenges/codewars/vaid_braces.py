def valid_braces(s):
    stack = []
    mapping = {"(": ")", "[": "]", "{": "}"}

    for char in s: # interaing over string
        if char in mapping: # checking if the current character is a key of mapping if it is it will append the value of the key in mapping to the stack
            stack.append(mapping[char])
        else: # if it is a closing brace it checks if the stack is empty or if the last element on the stack is the same as the current character in the iteration
            if not stack or stack.pop() != char: # if its not the same or the stack is empty it returns false
                return False

    return len(stack) == 0 # by the end of the iteration if every character had a matching closing character the stack should be empty if not return false


print(valid_braces("(){}[]"))