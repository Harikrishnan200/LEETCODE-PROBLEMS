# You are given a string consisting of uppercase English letters. Your task is to convert each unique letter (appearing 
# consecutively for the first time) into its corresponding position in the alphabet (i.e., 'A' → 1, 'B' → 2, ..., 'Z' → 26).
# However, if a letter appears consecutively more than once, replace its occurrence (except the first one) with an asterisk (*).





def solution(arr):
    prev = ""
    result = ""
    for i in arr:
        if i != prev:
            result += str(ord(i) - ord('A') + 1)
            prev = i
        else:
            result += '*'
    return result

print(solution("AAABBCCCC"))


# Another way to solve the problem



def convert(s):
    res = []
    for i in range(len(s)):
        if i == 0:
            res.append(ord(s[i])-64)
        elif s[i] == s[i-1]:
            res.append('*')
        else:
            res.append(ord(s[i])-64)
    return res



# Output
# 1**2*3***


