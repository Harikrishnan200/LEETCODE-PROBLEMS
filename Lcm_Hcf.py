# Find the lcm of a list of numbers



def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def lcm_of_list(nums):
    result = nums[0]
    for i in range(1, len(nums)):
        result = lcm(result, nums[i])
    return result

nums = [4, 6, 8]
print("LCM is:", lcm_of_list(nums))




# LCM is: 24
