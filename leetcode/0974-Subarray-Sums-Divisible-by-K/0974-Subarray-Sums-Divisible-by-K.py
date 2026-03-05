class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = {0:1}
        summ,count = 0,0
        for i in range(len(nums)):
            summ+=nums[i]

            if summ%k in pref:
                count+=pref[summ%k]
                
            pref[summ%k] = pref.get(summ%k,0) + 1
        
        return count