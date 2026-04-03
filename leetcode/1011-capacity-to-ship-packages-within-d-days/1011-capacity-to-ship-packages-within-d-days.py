class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(weight):
            nonlocal days
            count,summ,i = 0,0,0
            while i < len(weights):
                summ+=weights[i]
                if summ > weight:
                    summ-=weights[i]
                    if not summ:
                        return False
                    count+=1
                    summ = 0
                    continue
                i+=1
            if summ:
                count+=1
            return count <= days

        ans = 0
        l,r = 0,sum(weights)
        while l <= r:
            mid = (l+r)//2
            if check(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1

        return ans