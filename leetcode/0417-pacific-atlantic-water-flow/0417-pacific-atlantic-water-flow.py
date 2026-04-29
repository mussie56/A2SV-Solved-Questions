class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights),len(heights[0])
        pac = set()
        atl = set()
        # dir_pac = [(0,1),(1,0),(0,-1)]
        dir_ = [(0,-1),(-1,0),(0,1),(1,0)]

        def dfsPac(row,col,prev):
            nonlocal n,m
            if row < 0 or col < 0 or col >= m or row >= n or heights[row][col] < prev or (row,col) in pac:
                return
            pac.add((row,col))
            for r,c in dir_:
                new_row = row+r
                new_col = col+c
                dfsPac(new_row,new_col,heights[row][col])

        def dfsAtl(row,col,prev):
            nonlocal n,m
            if row < 0 or col < 0 or col >= m or row >= n or heights[row][col] < prev or (row,col) in atl:
                return
            atl.add((row,col))
            for r,c in dir_:
                new_row = row+r
                new_col = col+c
                dfsAtl(new_row,new_col,heights[row][col])


        for i in range(n):
            dfsPac(i,0,-1)
            dfsAtl(i,m-1,-1)
  
        for j in range(m):
            dfsPac(0,j,-1)
            dfsAtl(n-1,j,-1)

        ans = []

        for t in pac:
            if t in atl:
                i,j = t
                ans.append([i,j])

        return ans