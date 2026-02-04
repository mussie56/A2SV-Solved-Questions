class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = "@".join(source)
        i = 0
        while i < len(s)-1:
            if s[i]+s[i+1] == "//":
                j = i+2
                while j < len(s) and s[j]!="@":
                    j+=1
                s = s[:i]+s[j:]
            elif s[i]+s[i+1] == "/*":
                j = i+2
                while j < len(s)-1 and s[j]+s[j+1]!="*/":
                    j+=1
                s = s[:i]+s[j+2:]
            else:
                i+=1
              
        s = s.split('@')
        while "" in s:
            s.remove("")

        return s
