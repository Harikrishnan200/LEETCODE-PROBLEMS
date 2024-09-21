# Given an array of strings, group the anagrams together. You can return the answer in any order.  (LeetCode)

def group_anagrams(str):
    anagram_map = {}

    for word in str:
        key = ''.join(sorted(word))

        if key in anagram_map:
            anagram_map[key].append(word)
        else:
            anagram_map[key] = [word]

    return list(anagram_map.values())

print(group_anagrams(['abb', 'bba','eat','ate','eta','tan','nat']))

# output
# [['abb', 'bba'], ['eat', 'ate', 'eta'], ['tan', 'nat']]

# Time complexity : O(NKlogK) where N is the length of strs, and K is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.


