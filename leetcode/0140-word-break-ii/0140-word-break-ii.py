class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        n = len(s)
        wordDict = set(wordDict)
        def backtrack(ind,arr):
            nonlocal n
            if ind >= n:
                ans.append(" ".join(arr))
                return
            for i in range(ind,n):
                if s[ind:i+1] in wordDict:
                    arr.append(s[ind:i+1])
                    backtrack(i+1,arr)
                    arr.pop()

        backtrack(0,[])
        return ans