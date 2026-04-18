import numpy as np

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix) + 1 
        COLS = len(matrix[0]) + 1
        self.prefixes = [[0] * (COLS) for r in range(ROWS)]

        for row in range(1, ROWS):
            prefix = 0
            for col in range(1, COLS):
                prefix += matrix[row-1][col-1]
                above = self.prefixes[row-1][col]
                self.prefixes[row][col] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bigBlock = self.prefixes[row2+1][col2+1]
        rowToRemove = self.prefixes[row1][col2+1]
        colToremove = self.prefixes[row2+1][col1]
        valueToPutBackAgain = self.prefixes[row1][col1]

        return bigBlock - rowToRemove - colToremove + valueToPutBackAgain
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)