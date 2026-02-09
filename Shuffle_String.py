class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        merged = []
        for i in range(len(s)):
            merged.append([indices[i],s[i]])

        merged.sort()

        ans = []

        for i,j in merged:
            ans.append(j)

        return "".join(ans)
