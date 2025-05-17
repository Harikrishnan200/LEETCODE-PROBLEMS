def contiguous_subarrays(arr):
    result = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n + 1):
            result.append(arr[i:j])
    return result

# Example
arr = [1, 2, 3]
subsets = contiguous_subarrays(arr)
for s in subsets:
    print(s)



# Output:
# [1]
# [1, 2]
# [1, 2, 3]
# [2]
# [2, 3]
# [3]
