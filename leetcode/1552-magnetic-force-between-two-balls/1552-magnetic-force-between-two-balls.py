class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        def isValid(gap):
            nonlocal n,m
            count = 0
            j = 0
            for i in range(1,n):
                if position[i]-position[j] >= gap:
                    count +=1
                    j = i
                    
            return count >= m-1

        ans = 0
        l,r = 1,position[-1]-position[0]
        while l <= r:
            mid = (l+r)//2
            if isValid(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
                
        return ans