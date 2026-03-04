class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr,maxx = 0,float('-inf')

        for i in range(len(nums)):
            if curr < 0:
                curr = 0
            curr+=nums[i]
            maxx = max(maxx,curr)

        return maxx
