class Solution:
    def isAdditiveNumber(self, nums: str) -> bool:
        n = len(nums)
        def backtrack(ind,num):
            nonlocal n
            if len(num) > 2:
                if num[-1] != num[-3]+num[-2]:
                    return False
            if ind >= n:
                for i in range(2,len(num)):
                    if num[i] != num[i-1]+num[i-2]:
                        return False
                return True and len(num) > 2
                
            for i in range(ind,n):
                s = nums[ind:i+1]
                if s[0] == "0" and len(s)>1:
                    return False
                num.append(int(s))
                if backtrack(i+1,num):
                    return True
                num.pop()
            return False
            
        return backtrack(0,[])