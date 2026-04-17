class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])

        def backtrack(row: int,col: int):
            if row >= 9:
                return True
            if col == 9:
                return backtrack(row+1,0)
            if board[row][col] != ".":
                return backtrack(row,col+1)
                
            for i in range(1,10):
                num = str(i)
                if num in rows[row] or num in cols[col] or num in squares[(row//3,col//3)]:
                    continue
                rows[row].add(num)
                cols[col].add(num)
                squares[(row//3,col//3)].add(num)
                board[row][col] = num
                if backtrack(row,col+1):
                    return True
                board[row][col] = "."
                rows[row].remove(num)
                cols[col].remove(num)
                squares[(row//3,col//3)].remove(num)
            
            return False

        backtrack(0,0)