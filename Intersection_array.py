# You are given two integer arrays, nums1 and nums2, both not necessarily sorted.
# Return an array that represents their intersection, where each element in the result must appear as many times as it shows in both arrays.


# Test case 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Explanation: The intersection of nums1 and nums2 is 2, and it appears twice in nums1 and once in nums2.



from collections import Counter

def intersection_array(num1, num2):
    count1 = Counter(num1)
    count2 = Counter(num2)

    print(count1)
    print(count2)
    result = []

    for num in count1:
        if num in count2:
            result.extend([num] * min(count1[num], count2[num]))
    return result

num1 = [1, 2, 2, 1]
num2 = [2, 2,1]

print(intersection_array(num1,num2))



# If you want unique common elements (set intersection):

def intersection_set(num1, num2):
    return list(set(num1) & set(num2))

num1 = [1, 2, 2, 1]
num2 = [2, 2,1]
print(intersection_set(num1,num2))

# Output: [1,2]