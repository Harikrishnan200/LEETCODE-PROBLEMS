""" Given an array arr of n positive integers, your task is to find all the leaders in the array. An element of the array
is considered a leader if it is greater than all the elements on its right side or if it is equal to the maximum element
on its right side. The rightmost element is always a leader. (Geeks)"""

class Solution:

    def arrayLeaders(self, arr):
        list = []
        length = len(arr)
        for i in range(0,length):
            is_leader = True
            for j in range(i+1,length):
                if arr[i] <= arr[j]:
                    is_leader = False
                    break
            if is_leader:
                list.append(arr[i])
        return list

print(Solution().arrayLeaders([1, 2, 3,10, 5, 5, 3,7]))