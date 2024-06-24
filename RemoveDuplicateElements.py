"""
Given an array of numbers, remove the duplicate elements in the array and returned it. 
 """

class Solution:
    def removeDuplicateElements(self,lst:list[int]) ->list[int]:
        unique_list = []
        [unique_list.append(i) for i in lst if i not in unique_list]
        return unique_list


print(Solution().removeDuplicateElements([1,2,2,3]))


# using Set

def remove_duplicates(arr):
    return list(set(arr))

input_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(input_list)
print(unique_list)


# Using Dictionary

def remove_duplicates(arr):
    unique_list = []
    seen = {}
    for item in arr:
        if item not in seen:
            unique_list.append(item)
            seen[item] = True
    return unique_list

input_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(input_list)
print(unique_list)  
