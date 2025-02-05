# Leetcode 1
class solution:
    def twoSum(self,list: list[int],target: int)->list[int]:
        length = len(list)
        for i in range(length-1):
            for j in range(i+1,length):
                if list[i]+list[j] == target:
                    return [i,j]
        else:
            return -1
        
result = []        
obj = solution()
result= obj.twoSum([2,6,-6,15],9)        
print(result)       


# Using Hash map

def two_sum(arr, target):
    prev_map = dict()  # Hash map

    for i, num in enumerate(arr):
        if target - num in prev_map:
            return [i, prev_map[target - num]]
        else:
            prev_map[num] = i


print(two_sum([1, 7, 8, 3], 4))

# Time complexity: O(n)
# Space complexity: O(n)
