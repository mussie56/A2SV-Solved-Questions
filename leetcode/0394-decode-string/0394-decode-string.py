class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
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
                    # stack.pop()
                    return [ss,ind]
                ind+=1
        # for i in range(len(s)):
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
                # continue
                ans+=res[0]*n
            # else:
            #     return s
            i+=1
        # gen = helper(0,s)
        # return n*gen
        # def helper(ind:int, s:str) -> str:
        #     ss = ""
        #     while ind < len(s):
        #         if s[ind].isdigit():
        #             j = ind
        #             while s[i].isdigit():
        #                 ind+=1
        #             num = int(s[j:ind])
        #             ind-=1
        #         elif s[ind].isalpha():
        #             ss+=s[ind]
        #         elif s[ind] == "[":
        #             tmp = helper(ind+1,s)
        #             ind = tmp[1]
        #             ss+=tmp[0]*num
        #         else:
        #             # stack.pop()
        #             return [ss,ind]
        #         ind+=1

        return ans