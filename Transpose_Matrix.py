class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                arr[i][j] = matrix[j][i]

        return arr
