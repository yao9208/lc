class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, 0, i, j)==True:
                    return True
        return False

    def helper(self, board, word, idx, x, y):
        if idx==len(word):
            return True
        if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
            return False
        if board[x][y]==word[idx]:
            tmp = board[x][y]
            board[x][y]='.'
            if self.helper(board, word, idx+1, x+1, y)==True or self.helper(board, word, idx+1, x-1, y)==True or self.helper(board, word, idx+1, x, y+1)==True or self.helper(board, word, idx+1, x, y-1)==True:
                return True
            else:
                board[x][y]=tmp
        else:
            return False
        return False
