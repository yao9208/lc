class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        length = len(matrix) * len(matrix[0])
        start, end = 0, length-1
        while start <= end:
            mid = (start+end)/2
            m = mid/len(matrix[0])
            n = mid%len(matrix[0])
            if matrix[m][n]==target:
                return True
            elif matrix[m][n]>target:
                end = mid-1
            else:
                start = mid+1
        return False
