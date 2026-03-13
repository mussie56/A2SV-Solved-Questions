class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:(x[1]-x[0]))
        suma = 0
        l,r = 0,len(costs)-1
        while l <= r:
            suma+=costs[l][1]+costs[r][0]
            l+=1
            r-=1
        return suma