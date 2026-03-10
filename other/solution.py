class Solution:
    def decodeString(self, s: str) -> str:
        n = 0
        ans = ""
        def helper(ind:int, s:str) -> str:
            ss = ""
            while ind < len(s):
                if s[ind].isdigit():
                    j = ind
                    while s[ind].isdigit():
                        ind+=1
                    num = int(s[j:ind])
                    ind-=1
                elif s[ind].isalpha():
                    ss+=s[ind]
                elif s[ind] == "[":
                    tmp = helper(ind+1,s)
                    ind = tmp[1]
                    ss+=tmp[0]*num
                else:
                    return [ss,ind]
                ind+=1
                
        i,j = 0,0
        while i < len(s):
            if s[i].isdigit():
                j = i
                while s[i].isdigit():
                    i+=1
                n = int(s[j:i])
                i-=1
            elif s[i].isalpha():
                ans+=s[i]
            elif s[i] == "[":
                res = helper(i+1,s)
                i = res[1]
                ans+=res[0]*n
            i+=1

        return ans