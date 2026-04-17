class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minn = float('inf')
        n = len(cookies)
        ans = [0]*k
        def backtrack(ind):
            nonlocal minn,k
            if max(ans) >= minn:
                return
            if ind == n:
                minn = min(minn,max(ans))
                return
                
            for i in range(k):
                ans[i]+=cookies[ind]
                backtrack(ind+1)
                ans[i]-=cookies[ind]
                if ans[i] == 0:
                    break

        backtrack(0)
        return minn