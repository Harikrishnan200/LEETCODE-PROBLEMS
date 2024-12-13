# Problem: Given a list of non-negative integers, arrange them such that they form the smallest possible number.

# input = ['40', '5', '3', '0']
# output = 54030

from functools import cmp_to_key


def compare(x, y):
    """
    Custom comparator to determine the order of numbers.
    Compare concatenated results: x+y and y+x
    """
    if x + y > y + x:
        return -1  # x should come before y
    elif y + x > x + y:
        return 1  # y should come before x
    else:
        return 0  # x and y are equal


def largest_number(nums):
   
    str_nums = list(map(str, nums))

    # Sort numbers using the custom comparator
    sorted_nums = sorted(str_nums, key=cmp_to_key(compare))
    result = ''.join(sorted_nums)

    return result


nums = [40, 5, 3,0]
print("Largest Number:", largest_number(nums))

 