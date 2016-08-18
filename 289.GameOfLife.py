class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = self.count(board, i, j)
                if board[i][j]==1 and (count==2 or count==3):
                    board[i][j] = 3
                if board[i][j]==0 and count==3:
                    board[i][j] = 2
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


    def count(self, board, x, y):
        m, n = len(board), len(board[0])
        count = 0
        for i in range(max(0, x-1), min(m-1, x+1)+1):
            for j in range(max(0, y-1), min(n-1, y+1)+1):
                if board[i][j]&1==1:
                    count += 1
        count -= board[x][y]
        return count
