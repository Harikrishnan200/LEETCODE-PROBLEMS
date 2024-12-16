# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        result = []
        for i,num in enumerate(nums):
            if num == target:
                if len(result) >= 2:
                    result.pop(-1) 
                    result.append(i)
                else:
                    result.append(i)
        if len(result) == 1:
            temp = result[0]
            result.append(temp)
    
        return [-1,-1] if not result else result
    



def positions(nums, target):
    l, r = 0, len(nums) - 1  
    result = [-1, -1] 


    while l <= r:
        if nums[l] == target:
            result[0] = l
            break 
        l += 1
    
    while r >= l:  
        if nums[r] == target:
            result[1] = r
            break  
        r -= 1
    
    return result


nums = [5, 7, 7, 8, 8, 10]
target = 8
print(positions(nums, target))  

