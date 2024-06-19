""" Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements)
that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray. (Geeks)"""


class Solution:
    def indexesOfSubArraySum(self,list:list[int],sum:int,length:int)->list[int]:
        start = 0
        curr_sum = 0
        ans = []
        for end  in range(0,length):
            curr_sum += list[end]

            while curr_sum > sum and start <= end:
                curr_sum -= list[start]
                start += 1
            if curr_sum == sum:
                ans = [start + 1, end + 1]
                return ans
        else:
            ans = [-1]
            return ans


ans_list = []
ans_list = Solution().indexesOfSubArraySum(list=[1,2,3,4,5], sum=4, length=5)
print(ans_list)
