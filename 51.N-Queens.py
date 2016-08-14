class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        board = [0]*n
        self.search(result, board, n, 0)
        return result

    def search(self, result, board, n, row):
        if row==n:
            tmp = []
            for i in range(n):
                l = ['.']*n
                l[board[i]] = 'Q'
                tmp.append(''.join(l))
            result.append(tmp)
        for i in range(n):
            if self.isValid(board, row, i):
                board[row] = i
                self.search(result, board, n, row+1)
                board[row] = 0

    def isValid(self, board, x, y):
        n = len(board)
        for i in range(x):
            if board[i]==y:
                return False
            if abs(board[i]-y) == abs(i-x):
                return False
        return True
            
