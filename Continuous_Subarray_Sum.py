class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref = {0:-1}
        summ = 0
        for i in range(len(nums)):
            summ+=nums[i]
            if summ%k in pref:
                if i-pref[summ%k] >= 2:
                    return True
            else:
                pref[summ%k] = i

        return False
