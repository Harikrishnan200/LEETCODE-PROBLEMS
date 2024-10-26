def find_subarrays_with_sum(arr, target_sum, index=0, current=[]):
    if sum(current) == target_sum:
        print(current)
    
    for i in range(index, len(arr)):
        find_subarrays_with_sum(arr, target_sum, i + 1, current + [arr[i]])

# Example usage
arr = [1, 2, 3, 7, 5,12,11]
target_sum = 12
print(f"Subarrays with sum, {target_sum} :")
find_subarrays_with_sum(arr,target_sum)


# Output:
# Subarrays with sum, 12 :
# [1, 11]
# [2, 3, 7]
# [7, 5]
# [12]
