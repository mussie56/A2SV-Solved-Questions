class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0

        def dfs(row,col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0":
                return
            if visited[row][col]:
                return
            
            visited[row][col] = True
            grid[row][col] = "0"

            for r,c in directions:
                new_row = row+r
                new_col = col+c
                dfs(new_row,new_col)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count+=1
        return count