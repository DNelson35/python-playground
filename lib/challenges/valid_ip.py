# def is_valid_IP(s):
#     arr = s.split('.')
#     if len(arr) != 4: return False
#     for i in arr:
#         if i.isalpha() or i[0] == '0': return False
#         if int(i) not in range(0, 256):
#             return False
#     return True

# update to match test cases
def is_valid_IP(s):
    # Check for spaces in the string
    if " " in s: return False
    parts = s.split('.')
    # Check if the IP address has exactly four parts
    if len(parts) != 4: return False

    for part in parts:
        # Check if the part is a valid integer within the range 0-255
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
        # Check for leading zeros
        if part[0] == '0' and len(part) > 1:
            return False

    return True
print(is_valid_IP('01.02.3.66'))