def sub_array_with_product(arr, target_product, index=0, current=[]):
    # Calculate the product of the current combination
    current_product = 1
    for num in current:
        current_product *= num

    # Check if the product of the current combination equals the target
    if current_product == target_product:
        print(current)

    # Explore further combinations
    for i in range(index, len(arr)):
        sub_array_with_product(arr, target_product, i + 1, current + [arr[i]])


# Example usage
arr = [1, 2, 3, 4, 6]
target_product = 12
print("Non-Contiguous Subarrays with product", target_product, ":")
sub_array_with_product(arr,target_product)

# Output:
# Non-Contiguous Subarrays with product 12 :
# [1, 2, 6]
# [1, 3, 4]
# [2, 6]
# [3, 4]