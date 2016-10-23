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


public boolean isValidSudoku(char[][] board) {
    for(int i = 0; i<9; i++){
        HashSet<Character> rows = new HashSet<Character>();
        HashSet<Character> columns = new HashSet<Character>();
        HashSet<Character> cube = new HashSet<Character>();
        for (int j = 0; j < 9;j++){
            if(board[i][j]!='.' && !rows.add(board[i][j]))
                return false;
            if(board[j][i]!='.' && !columns.add(board[j][i]))
                return false;
            int RowIndex = 3*(i/3);
            int ColIndex = 3*(i%3);
            if(board[RowIndex + j/3][ColIndex + j%3]!='.' && !cube.add(board[RowIndex + j/3][ColIndex + j%3]))
                return false;
        }
    }
    return true;
}
