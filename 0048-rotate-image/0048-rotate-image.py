class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(i+1,columns):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        for i in range(rows):
            for j in range(columns // 2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][columns - 1 - j]
                matrix[i][columns - 1 - j] = temp