class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        def backtrack(ind,comb):
            nonlocal n
            ans.append(comb[:])
            if ind == n:
                return
            comb.append(nums[ind])
            backtrack(ind+1,comb)
            comb.pop()
            backtrack(ind+1,comb)

        backtrack(0,[])
        ans.sort()
        res = [ans[0]]
        for i in range(1,len(ans)):
            if ans[i] == res[-1]:
                continue
            res.append(ans[i])
        return res