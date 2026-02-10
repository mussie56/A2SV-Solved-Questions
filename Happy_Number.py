class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        
        while n not in visited:
            visited.add(n)
            s = str(n)
            nums = []
            for i in range(len(s)):
                nums.append(int(s[i]))

            n = 0
            for i in range(len(nums)):
                n+=(nums[i]**2)
            if n == 1:
                return True
                
        return False
