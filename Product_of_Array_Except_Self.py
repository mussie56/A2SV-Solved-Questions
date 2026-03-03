class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*n
        prefix = []
        suffix = [0]*n
        prefix.append(nums[0])
        suffix[n-1] = nums[n-1]
        for i in range(1,n):
            prefix.append(prefix[-1]*nums[i])
            suffix[n-1-i] = suffix[n-i]*nums[n-1-i]
            
        for i in range(n):
            if i == 0:
                ans[i] = suffix[i+1]
                continue
            if i == n-1:
                ans[i] = prefix[i-1]
                continue
            ans[i] = suffix[i+1]*prefix[i-1]
        return ans
