class solution:
    def twoSum(self,list: list[int],target: int)->list[int]:
        length = len(list)
        for i in range(length-1):
            for j in range(i+1,length):
                if list[i]+list[j] == target:
                    return [i,j]
        else:
            return -1
        
result = []        
obj = solution()
result= obj.twoSum([2,6,-6,15],9)        
print(result)       
        