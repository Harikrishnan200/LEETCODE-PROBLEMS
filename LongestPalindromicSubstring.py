def expand_around_center(s,left,right):
    # left -> minimum value is 0
    # right -> maximum value is len(s)-1
    # if s[left] == s[right] then compare the next characters
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1 : right]

def longest_palindrome(s):
    longest = ""
    for i in range(len(s)):
        # for odd length strings
        odd_palindrome = expand_around_center(s,i,i)
        # for even length strings
        even_palindrome = expand_around_center(s,i,i+1)

        longest = max(longest,odd_palindrome,even_palindrome, key=len)
    return longest

print(longest_palindrome("babad"))


# output
# 
# input : babad   (odd len string)
# output : bab    (even len string)
# 
# input : cbbd
# output : bb