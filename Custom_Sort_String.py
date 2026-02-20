class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapp = Counter(s)
        ans = []
        for i in order:
            if i in mapp:
                ans.append(i*mapp[i])
                del mapp[i]

        for i in mapp:
            ans.append(i*mapp[i])
            
        return "".join(ans)
