class Solution:
    def minSteps(self, s: str, t: str) -> int:
        maps = Counter(s)
        mapt = Counter(t)
        count = 0
        for i in maps:
            if i in t:
                if maps[i] > mapt[i]:
                    count+=maps[i]-mapt[i]
            else:
                count+=maps[i]

        return count
