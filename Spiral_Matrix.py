class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = set()
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        i = 0
        j = 0
        for _ in range((n+1)//2):
            while j < m and (i,j) not in visited:
                ans.append(matrix[i][j])
                visited.add((i,j))
                j+=1
            j-=1
            i+=1
            while i < n and (i,j) not in visited:
                ans.append(matrix[i][j])
                visited.add((i,j))
                i+=1
            i-=1
            j-=1
            while j >= 0 and (i,j) not in visited:
                ans.append(matrix[i][j])
                visited.add((i,j))
                j-=1
            j+=1
            i-=1
            while i >= 0 and (i,j) not in visited:
                ans.append(matrix[i][j])
                visited.add((i,j))
                i-=1
            i+=1
            j+=1

        return ans
