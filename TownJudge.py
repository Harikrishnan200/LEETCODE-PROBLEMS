# 997. Find the Town Judge

# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1



# Solution 1    

class Solution(object):
    def findJudge(self, n, trust):

        if n == 1 and not trust:
            return 1
            
        indegree = [0]*(n+1)   # Tracks how many people trust a particular person
        outdegree = [0]*(n+1)  # Tracks how many people a particular person trusts
        for a,b in trust:
            outdegree[a] += 1   
            indegree[b] += 1

        for i in range(n+1):
            if indegree[i] == n-1 and outdegree[i] == 0:
                return i
        else:
            return -1
        
        
# Solution 2


from collections import Counter
class Solution:
    def findJudge(self, n: int, t: list[int]) -> int:
        if n == 1:
            return 1

        x = {a for a,_ in t} # not judges
        c = Counter(b for _,b in t) # person: num of trusters
        for a, f in c.items():
            if f == n-1 and a not in x:
                return a
        
        return -1