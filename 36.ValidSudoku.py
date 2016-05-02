from sets import Set
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [Set() for x in range(9)]
        columns = [Set() for x in range(9)]
        box = [Set() for x in range(9)]

        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n=='.':
                    continue
                if n in rows[i]:
                    return False
                if n in columns[j]:
                    return False
                if n in box[(i//3)*3+j//3]:
                    return False
                rows[i].add(n)
                columns[j].add(n)
                box[(i//3)*3+j//3].add(n)
        return True
