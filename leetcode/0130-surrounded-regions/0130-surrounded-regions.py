class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        
        def dfs(row,col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] == "X":
                return
            
            if visited[row][col]:
                return 
                
            visited[row][col] = True
            board[row][col] = "Y"
            for r,c in directions:
                new_row = row+r
                new_col = col+c
                dfs(new_row,new_col)

        for j in range(len(board[0])):
            if board[0][j] == "O":
                board[0][j] = "T"
            if board[-1][j] == "O":
                board[-1][j] = "T"
        for i in range(len(board)):
            if board[i][0]=="O":
                board[i][0] = "T"
            if board[i][-1] == "O":
                board[i][-1] = "T"

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "T":
                    dfs(i,j)
                    
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"