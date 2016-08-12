from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board)==0 or len(board[0])==0:
            return
        m = len(board)
        n = len(board[0])
        if m < 3 or n < 3:
            return
        for i in (0, m-1):
            for j in range(n):
                if board[i][j]=='O':
                    self.bfs(board, i, j)
        for j in (0, n-1):
            for i in range(1, m-1):
                if board[i][j]=='O':
                    self.bfs(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='.':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'

    def bfs(self, board, x, y):
        m , n = len(board), len(board[0])
        if x<0 or x>=m or y<0 or y>=n:
            return
        queue = deque()
        if board[x][y]!='O':
            return
        val = x*n + y
        queue.append(val)
        while len(queue)!=0:
            tmp = queue.popleft()
            i,j = tmp/n, tmp%n
            board[i][j]='.'
            if i-1>=0 and board[i-1][j]=='O':
                queue.append((i-1)*n+j)
            if i+1<m and board[i+1][j]=='O':
                queue.append((i+1)*n+j)
            if j-1>=0 and board[i][j-1]=='O':
                queue.append(i*n+j-1)
            if j+1<n and board[i][j+1]=='O':
                queue.append(i*n+j+1)
            
