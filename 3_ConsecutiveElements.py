class Solution:
    def threeConsecutiveElements(self,list:list[int])->bool or bool and list[int]:
        length = len(list)
        ans = []
        for i in range(length - 2):
            if list[i] == list[i+1] == list[i+2]:
                ans.append(list[i])
                return True, ans
                
            else:
                return False
result,value = Solution().threeConsecutiveElements([1,1,1,2,2,6])                
if result: 
    print(value)
    print('yes')
    
else:
    print('no')
