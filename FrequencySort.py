# 5. Sorting by Frequency and Value

# Problem: Given a list of numbers, sort them in such a way that numbers that appear more frequently come first.
# If two numbers have the same frequency, the larger number should come first.

# input : nums = [1, 1, 2, 2, 2, 3, 3, 3, 3,10,10,10]
# output: [3, 3, 3, 3, 10, 10, 10, 2, 2, 2, 1, 1]


from collections import Counter
from functools import cmp_to_key

def compare(x, y):
    # Compare frequencies first
    count_x = freq[x]
    count_y = freq[y]
    if count_x > count_y:
        return -1  
    elif count_y > count_x:
        return 1
    else:
        # If frequencies are the same, compare the numbers themselves
        if x < y:
            return 1  # Larger numbers come first
        elif x > y:
            return -1
        else:
            return 0

def frequency_sort(nums):
    global freq
    freq = Counter(nums)  
    return sorted(nums, key=cmp_to_key(compare))

nums = [1, 1, 2, 2, 2, 3, 3, 3, 3]
print(frequency_sort(nums))  
