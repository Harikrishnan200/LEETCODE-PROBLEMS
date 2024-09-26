
# You are given an array arr of length n, and you can imagine this array repeating infinitely in both directions 
# (i.e., an infinite sequence where the array repeats itself over and over again).
# Given two integers L and R, find the sum of all elements between the indices L and R (1-based indexing) in this infinite array.


# 1 based indexing

def sum_in_infinite_array(arr, L, R):
    n = len(arr)

    # Convert L and R to 0-based indexing
    L -= 1
    R -= 1

    # Calculate the total sum of one complete array
    total_sum_of_array = sum(arr)

    # Calculate the number of full cycles
    full_cycles = (R // n) - (L // n) - 1

    # Calculate the sum
    sum_left_part = sum(arr[L % n:])  # From L to the end of the current cycle
    sum_right_part = sum(arr[:(R % n) + 1])  # From the start to R

    # Total sum
    total_sum = sum_left_part + sum_right_part + (full_cycles * total_sum_of_array)

    # If L and R are in the same cycle, adjust the total sum
    if L // n == R // n:
        total_sum = sum(arr[L % n:(R % n) + 1])

    return total_sum


# Example Usage
arr = [1, 2, 3]
L = 7
R = 15
print(sum_in_infinite_array(arr, L, R))  


# Output
# 18


#Solution of the same problem in 0-based indexing

def sum_in_infinite_array(arr, L, R):
    n = len(arr)

    
    # L -= 1
    # R -= 1

    # Calculate the total sum of one complete array
    total_sum_of_array = sum(arr)

    # Calculate the number of full cycles
    full_cycles = (R // n) - (L // n) - 1

    # Calculate the sum
    sum_left_part = sum(arr[L % n:])  # From L to the end of the current cycle
    sum_right_part = sum(arr[:(R % n) + 1])  # From the start to R

    # Total sum
    total_sum = sum_left_part + sum_right_part + (full_cycles * total_sum_of_array)

    # If L and R are in the same cycle, adjust the total sum
    if L // n == R // n:
        total_sum = sum(arr[L % n:(R % n) + 1])

    return total_sum


# Example Usage
arr = [1, 2, 3]
L = 7
R = 15
print(sum_in_infinite_array(arr, L, R))
