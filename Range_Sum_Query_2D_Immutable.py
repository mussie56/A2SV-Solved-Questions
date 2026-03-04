class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.pref[i][j] = matrix[i][j]
                if i > 0  and j > 0:
                    self.pref[i][j] += self.pref[i-1][j]+self.pref[i][j-1] - self.pref[i-1][j-1]
                elif i == 0 and j > 0:
                    self.pref[i][j] += self.pref[i][j-1]
                elif j ==0 and i > 0:
                    self.pref[i][j] += self.pref[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.pref[row2][col2]
        if row1 > 0 and col1 > 0:
            result -= self.pref[row1-1][col2] + self.pref[row2][col1-1] - self.pref[row1-1][col1-1]
        elif row1 == 0 and col1 > 0:
            result -= self.pref[row2][col1-1]
        elif col1 == 0 and row1 > 0:
            result -= self.pref[row1-1][col2]
        
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
