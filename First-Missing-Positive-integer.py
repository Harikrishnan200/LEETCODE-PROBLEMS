
#Given an unsorted integer array, find the first missing positive integer.

# TC = O(n)


# input: [3,4,-1,1,]
# output : 2


# optimised code
def first_missing_positive(arr):
    nums = set(arr)                   # Convert to a set for O(1) search
    for i in range(1, len(arr) + 2):  # Check up to len(arr) + 1
        if i not in nums:
            return i
    else:
        return None

arr = [3, 4, -1, 1, 5, 2]
print(first_missing_positive(arr))  


# Method 2  (Not Optimised)

# TC = O(mn)
def first_missing_positive_integer(arr):
    max_num = max(arr)
    for i in range(1,max_num+1):
        if i in arr:
            continue
        else:
            return i
    else:
        return None


arr = [3,4,-1,1,5,2]
print(first_missing_positive_integer(arr))
