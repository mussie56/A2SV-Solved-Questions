class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(pile):
            nonlocal k
            count = 0
            for i in candies:
                count += i//pile
            return count >= k
        l,r = 1,sum(candies)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1

        return ans