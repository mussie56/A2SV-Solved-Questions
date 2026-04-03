class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValidK(k: int):
            if k ==0:
                return False
            nonlocal h
            c = 0
            for i in range(len(piles)):
                c+=((piles[i]-1)//k)+1

            return c<=h

        l,r=0,max(piles)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if isValidK(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans