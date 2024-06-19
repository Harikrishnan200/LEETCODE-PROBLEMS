class Solution:
    def numberOfRectangles(self,radius:int)->int:
        diameter = 2*radius
        count = 0
        for i in range(1,diameter+1):  # length varies from 1 to 2r
            for j in range(1,diameter+1):   # width varies from 1 to 2r
                if (i**2 + j**2) <= (diameter**2):
                    count += 1
        return count

radius = int(input("Enter the radius of circle:"))
count = Solution().numberOfRectangles(radius)
if count is not None:
    print("Number of Rectangles that we have to cut is:"+str(count))
else:
    print("No rectangles can cut of from ths circle")
