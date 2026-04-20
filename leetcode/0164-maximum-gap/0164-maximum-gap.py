class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0

        low,high = min(nums),max(nums)
        if low == high:
            return 0
        bucket = [[] for i in range(len(nums))]
        
        for i in nums:
            bucket[int(((i-low)/(high-low))*(len(bucket)-1))].append(i)
        ans = []
        for i in bucket:
            if not i or i == []:
                continue
            ans+=sorted(i)
        
        maxx = 0
        for i in range(1,len(ans)):
            maxx = max(maxx,ans[i]-ans[i-1])
        
        return maxx