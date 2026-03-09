class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        mono = []
        ans = [0]*n
        for i in range(n-1,-1,-1):
            while mono and mono[-1][0] <= temperatures[i]:
                mono.pop()
            if mono:
                ans[i] = mono[-1][1]-i
            mono.append([temperatures[i],i])
        
        return ans