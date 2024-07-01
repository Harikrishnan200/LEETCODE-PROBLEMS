#Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list. (Geeks)

class Solution:
    def swap_any_elements(self,lst:list[int],pos1:int,pos2:int) ->list[int]:
        lst[pos1-1],lst[pos2-1] = lst[pos2-1],lst[pos1-1]
        return lst


print(Solution().swap_any_elements([1,2,3,4,5],1,3))

# Output:
[3, 2, 1, 4, 5]