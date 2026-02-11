class Solution:
    def frequencySort(self, s: str) -> str:
        mapp = Counter(s)
        
        s = list(mapp.items())
        
        s.sort(key=lambda x:-x[1])

        ans = []

        for i,ch in s:
            ans.append(ch*i)

        return "".join(ans)
