# Given a string S, return the number of permutations that can be formed by fixing the positions of vowels in the string.
# Example:
# Input: S = "ABC"
# Output: Vowel = 'A', rest = "BC". Therefore, the answer is 2! = 2.


def num_permutations(arr):
    consonents = [ch for ch in arr if ch.lower() not in {'a', 'e', 'i', 'o', 'u'}]
    count = len(consonents)
    
    fact = 1
    for i in range(1, count+1):
        fact *= i
    return fact

print(num_permutations("ABC")) # 2