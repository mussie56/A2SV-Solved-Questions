class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps = Counter(s)
        mapt = Counter(t)

        for i in maps:
            if i in mapt:
                if maps[i] != mapt[i]:
                    return False
            else:
                return False
        
        return True and len(maps) == len(mapt)
