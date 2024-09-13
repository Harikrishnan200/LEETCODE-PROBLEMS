# Given an array of size n , find the second largest element in the array. Else return -1 (geeks,leetcode)

class Solution:
    def print2largest(self, arr):
        larger = float('-inf')
        s_larger = float('-inf')

        for num in arr:
            if num > larger:
                s_larger = larger
                larger = num
            elif num > s_larger and num < larger:
                s_larger = num

        if larger == s_larger:
            return -1
        else:
            if s_larger == float('-inf'):
                return -1
            else:
                return s_larger

print(Solution().print2largest([10,10,2,5,7]))

# Output:

#7

# input [10,10] then return -1

# Another method

class Solution:
    def second_largest_number(self, lst: list[int]) -> int:
        sorted_array = sorted(lst, reverse=True) 
        second_largest = next((num for num in sorted_array if num < sorted_array[0]), None)  # next() fn returns the next item in an iterator.
        
        return second_largest

s_large = Solution().second_largest_number([1, 2, 3, 6, 8])
print("Second largest number in the given array is: " + str(s_large))
