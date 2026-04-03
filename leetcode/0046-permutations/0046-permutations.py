class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        visited = set()
        def backtrack(perm):
            nonlocal n
            if len(perm) == n:
                ans.append(perm[:])
                return

            for i in nums:
                if i not in visited:
                    visited.add(i)
                    perm.append(i)
                    backtrack(perm)
                    visited.remove(perm.pop())
                    
        backtrack([])
        return ans