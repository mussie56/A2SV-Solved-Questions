class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs[0]:
            return ""
        sub = strs[0][0]
        for i in range(1,len(strs[0])+1):
            sub = strs[0][:i]
            print(sub)
            for s in range(1,len(strs)):
                if sub != strs[s][:i]:
                    return sub[:-1]

        return sub
