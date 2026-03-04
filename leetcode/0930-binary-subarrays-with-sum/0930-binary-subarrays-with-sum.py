class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pref = {0:1}
        summ,count = 0,0
        for i in range(len(nums)):
            summ+=nums[i]

            if summ-goal in pref:
                count+=pref[summ-goal]

            pref[summ] = pref.get(summ,0)+1

        return count