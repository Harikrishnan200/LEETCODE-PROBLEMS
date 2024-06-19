# Solution 1  TC -> O(n^2)

class Solution:

    # Note that the size of the array is n-1
    def missingElement(self,arr):
        count = False
        list = []
        length = len(arr)
        for i in range(0,length-1):
            for j in range(i+1,length):
                if arr[i] == arr[j]:
                    count = True
                    list.append(arr[i])
        if count:
            return list
        else:
            return [-1]





print(Solution().missingElement( [1, 2, 3, 5,5,3]))

# Optimized Solution

class Solution:
    
        # Note that the size of the array is n-1
        def missingElement(self,arr):
            count = False
            list = []
            length = len(arr)
            arr.sort()
            for i in range(0,length-1):
                if arr[i] == arr[i+1]:
                    count = True
                    list.append(arr[i])
            if count:
                return list
            else:
                return [-1]

print(Solution().missingElement( [1, 2, 3, 5,5,3]))            
