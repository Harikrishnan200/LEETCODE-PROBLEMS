# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.



class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        swap = 0
        if not s1 or not s2 or len(s1) != len(s2):
            return False     
        else:
            if s1 == s2:
                return True
            swap = []
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    swap.append((s1[i],s2[i])) 
                
            if len(swap) > 2:
                return False
            return len(swap) == 2 and swap[0] == swap[1][::-1]
        


# Another approach

def areAlmostEqual(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    # Find indices where characters differ
    diff = [(a, b) for a, b in zip(s1, s2) if a != b]

    # There should be exactly 2 differing positions, and swapping should fix it
    return len(diff) == 2 and diff[0] == diff[1][::-1]