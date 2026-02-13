class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) == len(pattern):
            merged = set()
            for i in range(len(pattern)):
                merged.add((pattern[i],s[i]))

            return len(merged) == len(set(pattern)) and len(merged) == len(set(s))
        return False
