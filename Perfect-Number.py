# A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. 
# A divisor of an integer x is an integer that can divide x evenly.

# Given an integer n, return true if n is a perfect number, otherwise return false.

# Input: num = 28

# Output: true


# Explanation: The divisors of 28 are 1, 2, 4,
# 7, 14, and 28. 
# 1 + 2 + 4 + 7 + 14 = 28, so 28 is a perfect number.

def perfect_number(num):
    divisors = []
    for i in range(1,num):
        if num%i == 0:
            divisors.append(i)
    return sum(divisors) == num

num = 17
print(perfect_number(num))


