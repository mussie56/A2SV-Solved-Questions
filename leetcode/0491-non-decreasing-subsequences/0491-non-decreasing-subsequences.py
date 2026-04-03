class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(ind,sub):
            if len(sub) > 1:
                for i in range(1,len(sub)):
                    if sub[i] < sub[i-1]:
                        return
                ans.append(sub[:])
            if ind >= n:
                return

            sub.append(nums[ind])
            backtrack(ind+1,sub)
            sub.pop()
            backtrack(ind+1,sub)
        
        backtrack(0,[])
        if not ans:
            return []
        ans.sort()
        res = [ans[0]]
        for i in range(1,len(ans)):
            if ans[i] == res[-1]:
                continue
            res.append(ans[i])
        return res