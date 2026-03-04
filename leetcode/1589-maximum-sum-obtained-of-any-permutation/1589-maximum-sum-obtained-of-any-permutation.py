class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 1000000007
        nums.sort(reverse=True)
        pref = [0]*(len(nums)+1)
        for l,r in requests:
            pref[l] += 1
            pref[r+1] -= 1

        for i in range(1,len(pref)):
            pref[i]+=pref[i-1]
        pref.sort(reverse=True)
        summ = 0
        for i in range(len(nums)):
            summ+=(pref[i]*nums[i])
        
        return summ%mod