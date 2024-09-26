# LeetCode  

# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

def unique_character(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for index,char in enumerate(s):
        if char_count[char] == 1:
            return index
    else:
        return -1

print(unique_character("hhaai"))

# output
# 4