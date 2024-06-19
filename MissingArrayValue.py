class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        sum_n = n*(n+1)//2
        sum_arr = sum(arr)
        missing_value = sum_n - sum_arr
        return missing_value
  
print(Solution().missingNumber(5,[1,2,3,5]))