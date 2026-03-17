class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count,i=0,0
        summ = 1
        while summ<=n:
            if i < len(nums) and nums[i] <= summ:
                summ+=nums[i]
                i+=1
            else:
                summ*=2
                count+=1

        return count