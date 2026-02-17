class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        if mat == target:
            return True
        for _ in range(3):
            visited = set()
            for i in range(n):
                for j in range(n):
                    if (i,j) not in visited:
                        mat[i][j], mat[j][i] = mat[j][i],mat[i][j]
                        visited.add((i,j))
                        visited.add((j,i))
                        
            for i in range(n):
                for j in range(n//2):
                    mat[i][j], mat[i][n-j-1] = mat[i][n-j-1],mat[i][j]
            if mat == target:
                return True
        return False
