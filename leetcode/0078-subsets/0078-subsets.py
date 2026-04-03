class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def backtrack(start,subset):
            nonlocal n
            if len(subset) > n:
                return
            ans.append(subset[:])
            for i in range(start,n):
                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()

        backtrack(0,[])
        return ans