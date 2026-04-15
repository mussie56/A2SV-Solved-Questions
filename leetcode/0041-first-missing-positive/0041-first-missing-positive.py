class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mapp = set()
        for i in nums:
            if i > 0:
                mapp.add(i)
        
        for i in range(1,len(nums)+1):
            if i not in mapp:
                return i
        return len(nums)+1