# You are in a grocery store and have a list of items, A, of size N. In one operation,
# you can swap any two items on the list. Find and return the minimum possible sum of any two 
# consecutive items on the list after performing any number of such operations.
# Example:
# Input: input1 = 3 (number of items), input2 = [3, 5, 1] (list of items)
# Output: Minimum possible sum of consecutive elements = 4


def min_consecutive_sum(arr):
    arr.sort()
    return arr[0] + arr[1]

print(min_consecutive_sum([3, 5, 1])) # 4


# Time complexity: O(nlogn) where n is the number of items in the list


#ANOTHER SOLUTION

def min_consecutive_sum(arr):
    arr.sort()
    min_sum = float('inf')
    for num in range(len(arr)-1):
        min_sum = min(min_sum, arr[num]+arr[num+1])
    return min_sum

print(min_consecutive_sum([3, 5, 1])) # 4

# Time complexity: O(nlogn) where n is the number of items in the list