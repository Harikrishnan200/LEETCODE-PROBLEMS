
# Find all contiguous sub array with given sum

#input :
#arr = [1, 2, 3, 7, 5, 12, 11]
#target_sum = 12

#output:
#[2, 3, 7]
#[7, 5]
#[12]


def find_all_contiguous_subarrays_with_sum(arr, target_sum):
    for start in range(len(arr)):
        current_sum = 0
        for end in range(start, len(arr)):
            current_sum += arr[end]
            if current_sum > target_sum:
                break
            elif current_sum == target_sum:
                print(arr[start:end + 1])

# Example usage
arr = [1, 2, 3, 7, 5, 12, 11]
target_sum = 12
print(f"All contiguous subarrays with sum {target_sum}:")
find_all_contiguous_subarrays_with_sum(arr, target_sum)
