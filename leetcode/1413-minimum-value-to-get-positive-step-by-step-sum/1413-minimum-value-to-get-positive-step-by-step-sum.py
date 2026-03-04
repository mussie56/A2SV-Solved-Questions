class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pref = [nums[0]]
        minn = nums[0]
        for i in range(1,len(nums)):
            pref.append(pref[-1]+nums[i])
            minn = min(minn,pref[-1])
        
        return abs(minn)+1 if minn < 0 else 1