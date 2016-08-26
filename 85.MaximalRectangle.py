class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        result = 0
        if len(matrix)==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        left, right, height = [0]*n, [n]*n, [0]*n
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j]=='1':
                    height[j] += 1
                else:
                    height[j] = 0
            for j in range(n):
                if matrix[i][j]=='1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j+1
            for j in range(n-1, -1, -1):
                if matrix[i][j]=='1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                cur_area = (right[j]-left[j])*height[j]
                result = max(result, cur_area)
        return result
