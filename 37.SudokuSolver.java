public class Solution {
    public void solveSudoku(char[][] board) {
        solve(board);
    }
    public boolean solve(char[][] board){
        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                if(board[i][j]=='.'){
                    for(char c='1'; c<='9'; c++){
                        if(isValid(board, i,j, c)){
                            board[i][j]=c;
                            if(solve(board)){
                                return true;
                            }else{
                                board[i][j]='.';
                            }
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }
    public boolean isValid(char[][] board, int x, int y, char c){
        for(int i=0; i<9; i++){
            if(board[i][y]==c||board[x][i]==c){
                return false;
            }
        }
        for(int i=(x/3)*3; i<(x/3)*3+3; i++){
            for(int j=(y/3)*3; j<(y/3)*3+3; j++){
                if(board[i][j]==c){
                    return false;
                }
            }
        }
        return true;
    }
}
