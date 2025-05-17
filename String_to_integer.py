# converts a string to an integer, mimicking the behavior of the atoi function in C.



def my_atoi(s):
    s = s.strip()   # Remove leading spaces
    if not s:
        return 0    # If the string is empty after stripping, return 0
    
    sign = -1 if s[0] == '-' else 1  # Set the sign: negative if s[0] == '-', otherwise positive
    
    if s[0] in ['-', '+']:
        s = s[1:]  # Remove the sign character if it's there
    
    result = 0
    for ch in s:
        if ch.isdigit():                  # Only consider numeric characters
            result = result * 10 + int(ch)  # Shift previous digits left and add new digit
        else:
            break  # Stop at first non-digit character
    
    return sign * result  # Return final result with sign


print(my_atoi("   -42abc"))  # Output: -42