class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix)==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        result = 0
        cache = [[0]*n for x in range(m)]
        for i in range(m):
            for j in range(n):
                result = max(result, self.dfs(matrix, cache, i, j))
        return result

    def dfs(self, matrix, cache, x, y):
        dir = [[0,1],[0,-1],[-1,0],[1,0]]
        if cache[x][y]!=0:
            return cache[x][y]
        result = 1
        for d in dir:
            i, j = x+d[0], y+d[1]
            if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]<=matrix[x][y]:
                continue
            result = max(result, 1+self.dfs(matrix, cache, i, j))
        cache[x][y] = result
        return result
