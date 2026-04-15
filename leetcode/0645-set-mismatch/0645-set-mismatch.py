class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mapp = set()
        ans = []
        for i in nums:
            if i in mapp:
                ans.append(i)
                continue
            mapp.add(i)
        
        for i in range(1,len(nums)+1):
            if i not in mapp:
                ans.append(i)
                break
        
        return ans