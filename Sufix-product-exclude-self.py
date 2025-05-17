def suffix_product_exclude_self(arr):
    n = len(arr)
    result = [1] * n   # important to initialize with 1
    suffix = 1

    for i in range(n - 1, -1, -1):
        result[i] = suffix
        suffix *= arr[i]

    return result

# Test
arr = [2, 3, 4, 5]
print(suffix_product_exclude_self(arr)) 



# op: [60, 20, 5, 1]