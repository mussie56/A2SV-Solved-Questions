class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def findClosest(heaters: List[int], target: int) -> int:
            l,r=0,len(heaters)-1
            while l+1 < r:
                mid = (l+r)//2
                if heaters[mid] == target:
                    return heaters[mid]
                elif heaters[mid] > target:
                    r = mid
                else:
                    l = mid
            if abs(heaters[l]-target) < abs(heaters[r]-target):
                return heaters[l]
            return heaters[r]

        maxx = 0
        for i in houses:
            maxx = max(maxx,abs(i-findClosest(heaters,i)))
            
        return maxx