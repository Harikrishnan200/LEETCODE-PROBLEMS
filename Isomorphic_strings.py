# Two strings s1 and s2 are called isomorphic if there is a one-to-one mapping possible for every character of s1 to
# every character of s2. And all occurrences of every character in ‘s1’ map to the same character in ‘s2’.

# Examples: 

# Input:  s1 = “aab”, s2 = “xxy”
# Output: True
# Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.


# Input:  s1 = “aab”, s2 = “xyz”
# Output: False
# Explanation: One occurrence of ‘a’ in s1 has ‘x’ in s2 and other occurrence of ‘a’ has ‘y’.



def are_isomorphic(s1, s2):
    if len(s1) != len(s2):
        return False

    map_s1_to_s2 = {}
    map_s2_to_s1 = {}

    for ch1, ch2 in zip(s1, s2):
        if ch1 in map_s1_to_s2:
            if map_s1_to_s2[ch1] != ch2:
                return False
        else:
            map_s1_to_s2[ch1] = ch2

        if ch2 in map_s2_to_s1:
            if map_s2_to_s1[ch2] != ch1:
                return False
        else:
            map_s2_to_s1[ch2] = ch1

    return True


print(are_isomorphic("aab", "xxy"))  # Output: True
print(are_isomorphic("aab", "xyz"))  # Output: False




# map_s1_to_s2 ensures that every character in s1 maps consistently to s2.
# map_s2_to_s1 ensures no two characters in s1 map to the same character in s2.