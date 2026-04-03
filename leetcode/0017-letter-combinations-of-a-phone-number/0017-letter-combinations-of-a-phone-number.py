class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapp = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        n = len(digits)
        ans = []
        def backtrack(ind,comb):
            nonlocal n
            if ind > n:
                return
            if len(comb) == n:
                ans.append("".join(comb))
                return
            for i in mapp[digits[ind]]:
                comb.append(i)
                backtrack(ind+1,comb)
                comb.pop()
        backtrack(0,[])
        return ans