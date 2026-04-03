class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        def backtrack(ind,split):
            nonlocal n
            if ind >= n:
                for i in range(len(split)-1):
                    if split[i] != split[i+1]+1:
                        return False
                return len(split) >= 2
                
            for i in range(ind,n):
                split.append(int(s[ind:i+1]))
                if backtrack(i+1,split):
                    return True 
                split.pop()
            
            return False

        return backtrack(0,[])