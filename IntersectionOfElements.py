# Given two integer arrays arr1 and arr2, return an array of their intersection. Each element in the result must be 
# unique, and the result can be in any order.  (LeetCode)

# SOLUTION 1

def intersection(arr1,arr2):
    result = set()
    tot_arr = arr1 + arr2
    tot_len = len(tot_arr)

    for i in range(tot_len):
        if tot_arr[i] in arr1 and tot_arr[i] in arr2:
            result.add(tot_arr[i])

    return list(result)


print(intersection([1,2,3,5,7],[2,3,4,1,8]))

# SOLUTION 2  (using hash map)

def intersection(arr1,arr2):
    hash_map = {}
    result = set()

    for num in arr1:
        if num not in hash_map:
            hash_map[num] = 1


    for num in arr2:
        if num in hash_map:
            result.add(num)

    return list(result)

print(intersection([1,2,3,5,7],[2,3,4,1,8]))


# SOLUTION 3

def intersection(arr1,arr2):
    return list(set(arr1) & set(arr2))      # ( intersection of two sets )

print(intersection([1,2,3,5,7],[2,3,4,1,8]))



# Input : [1,2,3,5,7],[2,3,4,1,8]
# Output : [1,2,3]
