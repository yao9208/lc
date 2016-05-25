class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(matrix)*len(matrix[0])-1
        while start < end:
            mid = start + (end-start)/2
            m = mid/len(matrix[0])
            n = mid%len(matrix[0])
            val = matrix[m][n]
            if val==target:
                return True
            if val < target:
                start = mid+1
            else:
                end = mid - 1
        if matrix[start/len(matrix[0])][start%len(matrix[0])]==target:
            return True
        return False
