# Given an array of size n , find the second largest element in the array.

class Solution:
    def second_largest_number(self,lst:list[int]) ->int:
        first_num = float('-inf')  # first_num is initially assigned to neg infinity
        second_num = float('-inf')
        for num in lst:
            if num > first_num:
                second_num = first_num
                first_num = num
            elif num > second_num and num != first_num:
                second_num = num

        return second_num
s_large = Solution().second_largest_number([1,2,3,6,8])
print("Second largest num in the given array is:"+str(s_large))

# Output:

# Second largest num in the given array is:6