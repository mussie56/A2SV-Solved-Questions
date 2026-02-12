class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_note = Counter(ransomNote)
        mag = Counter(magazine)

        for i in r_note:
            if i in mag:
                if r_note[i] > mag[i]:
                    return False
            else:
                return False

        return True
