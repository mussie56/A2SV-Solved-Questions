class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i = 0
        while i < len(s)-1:
            if roman[s[i]] < roman[s[i+1]]:
                ans += roman[s[i+1]] - roman[s[i]]
                i+=2
            else:
                ans += roman[s[i]]
                i+=1
        if i < len(s):
            ans += roman[s[i]]
        return ans
