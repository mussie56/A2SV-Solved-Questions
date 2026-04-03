class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(start,comb):
            nonlocal k
            nonlocal n
            if len(comb) == k:
                ans.append(comb[:]) #since comb is a reference at the end it'll become [] making everything [] so we copy instead
                return
            for nc in range(start,n+1):
                comb.append(nc)
                backtrack(nc+1,comb)
                comb.pop()
                
        backtrack(1,[])
        return ans