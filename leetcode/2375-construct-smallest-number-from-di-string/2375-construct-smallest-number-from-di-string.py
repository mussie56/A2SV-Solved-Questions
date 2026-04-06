class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        n = len(pattern)
        visited = set()
        def backtrack(arr):
            nonlocal n
            if len(arr) == n+1:
                k = 0
                for i in range(1,len(arr)):
                    if pattern[k] == "I" and int(arr[i]) < int(arr[i-1]) or pattern[k] == "D" and int(arr[i]) > int(arr[i-1]):
                        return False
                    k+=1
                ans.append("".join(arr))
                return True
            if len(arr) > n:
                return False
            
            for i in range(1,n+2):
                if i not in visited:
                    visited.add(i)
                    arr.append(str(i))
                    if backtrack(arr):
                        return True
                    arr.pop()
                    visited.remove(i)
            return False

        backtrack([])
        return ans[0]