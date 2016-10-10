class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0:
            return []
        m, n = len(matrix), len(matrix[0])
        visited = [[0]*n for x in range(m)]
        result = []
        for i in range(m):
            self.dfs(matrix, i, 0, matrix[i][0], visited, 1, result)
            self.dfs(matrix, i, n-1, matrix[i][n-1], visited, 2, result)
        for j in range(0, n):
            self.dfs(matrix, 0, j, matrix[0][j], visited, 1, result)
            self.dfs(matrix, m-1, j, matrix[m-1][j], visited, 2, result)
        return result

    def dfs(self, matrix, x, y, pre, visited, flag, result):
        m, n = len(matrix), len(matrix[0])
        if x<0 or x>=m or y<0 or y>=n or pre>matrix[x][y] or (visited[x][y]&flag)==flag:
            return
        visited[x][y] |= flag
        if visited[x][y]==3:
            result.append([x, y])
        self.dfs(matrix, x+1, y, matrix[x][y], visited, visited[x][y], result)
        self.dfs(matrix, x, y+1, matrix[x][y], visited, visited[x][y], result)
        self.dfs(matrix, x-1, y, matrix[x][y], visited, visited[x][y], result)
        self.dfs(matrix, x, y-1, matrix[x][y], visited, visited[x][y], result)
