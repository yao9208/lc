class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid is None or len(obstacleGrid)==0:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        board = [[0 for i in range(n)] for i in range(m)]
        num = 1
        for i in range(n):
            if obstacleGrid[0][i]==1:
                num = 0
            board[0][i] = num
        num = 1
        for i in range(m):
            if obstacleGrid[i][0]==1:
                num=0
            board[i][0] = num
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]==1:
                    board[i][j] = 0
                else:
                    board[i][j] = board[i-1][j] + board[i][j-1]
        return board[m-1][n-1]
