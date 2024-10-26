#  You are given an array of integers. Your task is to determine the minimum number of operations 
# required to sort the array in non-decreasing order. In a single operation, you can remove an element that 
# is greater than the element immediately following it.


def min_operations_to_sort(arr):
    count = 0
    
    while arr != sorted(arr):  # Keep doing operations until the array is sorted
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]: 
                arr.pop(i + 1)  
                count += 1 
                break 
    
    return count


arr1 = [3, 6, 4, 1]
print(min_operations_to_sort(arr1))  # Output: 2

arr2 = [7, 5, 2, 8, 1]
print(min_operations_to_sort(arr2))  # Output: 3



# ANOTHER METHOD  (EFFICIENT)


import bisect

def length_of_LIS(arr):
    # This will hold the smallest tail of all increasing subsequences
    lis = []
    
    for num in arr:
        # Find the index of the smallest number in lis which is >= num
        index = bisect.bisect_left(lis, num)
        
        # If num is greater than all elements in lis
        if index == len(lis):
            lis.append(num)  # Extend the size of LIS
        else:
            lis[index] = num  # Update the existing index
    
    return len(lis)

def min_operations_to_sort(arr):
    # Calculate the length of the longest increasing subsequence
    lis_length = length_of_LIS(arr)
    
    # The minimum operations needed is the size of the array minus the LIS length
    return len(arr) - lis_length

# Test cases
arr1 = [3, 6, 4, 1]
print(min_operations_to_sort(arr1))  # Output: 2

arr2 = [7, 5, 2, 8, 1]
print(min_operations_to_sort(arr2))  # Output: 3
