
# You are given an array of positive integers. Your task is to find the largest Least Common Multiple (LCM)
# that can be formed by two consecutive elements in the array.  ( asked in UST)
#
# split the array into sets like
# arr1 = [3, 6, 4, 1]
# sets = {{3,6},{6,4},{4,1}}
# then return the largest LCM


import math

result = []
def lcm_of_two_numbs(a, b):
    return abs(a * b) // math.gcd(a, b)

def largest_lcm(arr):
    for i in range(len(arr)-1):
        num1 = arr[i]
        num2 = arr[i+1]
        
        lcm =  lcm_of_two_numbs(num1,num2)
        result.append(lcm)
   
    return max(result) if result else [-1]


arr1 = [3, 6, 4, 1]
print(largest_lcm(arr1))  # Output: 12


arr2 = [7, 5, 2, 8, 1]
print(largest_lcm(arr2))  # Output: 56
