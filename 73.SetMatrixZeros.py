class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        tmp = 1
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                tmp = 0
        for i in range(len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(len(matrix)-1, -1, -1):
            for j in range(len(matrix[0])-1, 0, -1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            if tmp==0:
                matrix[i][0]=0

        
