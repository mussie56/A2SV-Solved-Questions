class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        summ = 0
        j = 0
        maxx = 0
        for i in range(len(nums)):
            summ+=nums[i]
            while j < len(nums) and summ < i-j:
                summ-=nums[j]
                j+=1
                
            maxx = max(maxx,summ)
        if maxx == len(nums):
            maxx-=1
        return maxx
