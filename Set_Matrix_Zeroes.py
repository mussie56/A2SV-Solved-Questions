class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        seti = set()
        setj = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    seti.add(i)
                    setj.add(j)

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in seti:
                    matrix[i][j] = 0
                    continue
                    
                if j in setj:
                    matrix[i][j] = 0
