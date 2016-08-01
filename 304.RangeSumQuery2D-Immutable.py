class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            self.matrix = matrix
            return
        m, n = len(matrix), len(matrix[0])
        for i in range(1, n):
            matrix[0][i] += matrix[0][i-1]
        for i in range(1, m):
            matrix[i][0] += matrix[i-1][0]
        for i in range(1, m):
            for j in range(1, n):
                matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]
        self.matrix = matrix


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if len(self.matrix)==0:
            return 0
        top = self.get(row1-1, col2)
        left = self.get(row2, col1-1)
        topleft = self.get(row1-1, col1-1)
        return self.get(row2, col2)-top-left+topleft

    def get(self, row, col):
        if row<0 or col<0:
            return 0
        return self.matrix[row][col]



# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
