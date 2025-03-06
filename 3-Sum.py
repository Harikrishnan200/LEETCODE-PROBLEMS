# 15. 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.


# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for i in range(len(nums)-2):
            first_num = nums[i]
            j = i + 1
            k = len(nums)-1
            while j < k:
                second_num = nums[j]
                third_num = nums[k]
                tot_sum = first_num + second_num + third_num
                
                if tot_sum > 0:
                    k -= 1
                elif tot_sum < 0:
                    j += 1
                elif tot_sum == 0:
                    result.add((first_num,second_num,third_num))
                    j += 1
                    k -= 1
                
        return list(result)



