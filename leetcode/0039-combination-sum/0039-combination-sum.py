class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(start,comb):
            nonlocal target
            if sum(comb) > target:
                return True
            if sum(comb) == target:
                ans.append(comb[:])
                return True
            minn = min(candidates)
            for i in range(start,len(candidates)):
                comb.append(candidates[i])
                ret = backtrack(i,comb)
                comb.pop()
                if ret:
                    break

        backtrack(0,[])
        return ans