class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        s = "abc"
        def helper(happy):
            nonlocal n
            if len(happy) == n:
                ans.append("".join(happy))
                return
            for i in s:
                if happy and happy[-1] == i:
                    continue
                happy.append(i)
                helper(happy)
                happy.pop()

        helper([])
        ans.sort()
        if k > len(ans):
            return ""
        return ans[k-1]