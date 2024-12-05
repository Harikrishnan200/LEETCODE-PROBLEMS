def isValid(s: str) -> bool:
    bracket_map = {')': '(', '}': '{', ']': '['}  # set the closed brackets as keys and opening brackets as its values
    stack = []

    for char in s:
        if char in bracket_map:           # if the char is a closed bracket
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        elif char in bracket_map.values():    # if the char is an openning bracket
            stack.append(char)

    return not stack


# Test case
print(isValid("{[][(())]}"))  # Output: True