# Given a string s, find the length of the longest substring without repeating characters.

def longest_palindromic_substring(str):
    char_index = {}
    left = 0
    max_length = 0

    for right in range(len(str)):
        char = str[right]

        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1

        char_index[char] = right

        max_length = max(max_length,right - left +1)
    return max_length

print(longest_palindromic_substring("abaabcbb"))


# output

# input : abaabcbb
# output : 3

# input : abac
# output : 3