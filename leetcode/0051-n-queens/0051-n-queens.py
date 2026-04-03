class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = set()
        rDiag = set()
        lDiag = set()
        ans = []
        def backtrack(i,mat):
            nonlocal n
            if len(mat) == n:
                ans.append(mat[:])
                return
            if i > n:
                return
                
            temp = ['.']*n
            for j in range(n):
                if j not in columns and i-j not in rDiag and i+j not in lDiag:
                    columns.add(j)
                    rDiag.add(i-j)
                    lDiag.add(i+j)
                    temp[j] = "Q"
                    mat.append("".join(temp))
                    backtrack(i+1,mat)
                    mat.pop()
                    temp[j] = '.'
                    columns.remove(j)
                    rDiag.remove(i-j)
                    lDiag.remove(i+j)
        backtrack(0,[])
        return ans