
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears 
# exactly once. Find this single element that appears only once. (asked in Mitsogo)
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2

# METHOD 1 (TC->O(n))

def singleNonDuplicate(nums):


    total_sum = sum(nums)
    unique_sum = sum(set(nums))

    return 2 * unique_sum - total_sum


nums = [3, 3, 7, 7, 10, 11, 11]
result = singleNonDuplicate(nums)
print(result)  

# METHOD 2 (TC->O(logn))  (Efficient)
def singleNonDuplicate(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid + 1]:
            left = mid + 2
        else:
            right = mid
    return nums[left]
nums = [3, 3, 7, 7, 10, 11,
        11]
result = singleNonDuplicate(nums)
print(result)


# METHOD 3 (TC->O(n))

def singleNonDuplicate(nums):
    for i in range(0, len(nums), 2):
        if i + 1 == len(nums):
            return nums[i]
        if nums[i] != nums[i + 1]:
            return nums[i]
nums = [3, 3, 7, 7, 10, 11,
        11]
result = singleNonDuplicate(nums)
print(result)



# METHOD 4 (TC->O(n))

def singleNonDuplicate(nums):
    return sum(set(nums)) * 2 - sum(nums)
nums = [3, 3, 7, 7, 10, 11,
        11]
result = singleNonDuplicate(nums)
print(result)


