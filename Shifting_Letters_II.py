class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0]*(len(s)+1)

        for l,r,k in shifts:
            if k == 1:
                pref[l] += 1
                pref[r+1] -=1
            else:
                pref[l] -=1
                pref[r+1] +=1
                
        summ = 0
        ans = []
        for i in range(len(s)):
            summ+=pref[i]
            ch = ord(s[i]) - 97
            ans.append(chr((ch + summ)%26 + 97))

        return "".join(ans)
