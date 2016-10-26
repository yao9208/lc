public class Solution {
    public int maxKilledEnemies(char[][] grid) {
        if(grid==null || grid.length==0 || grid[0].length==0){
            return 0;
        }
        int row = 0;
        int[] col = new int[grid[0].length];
        int result = 0;
        for(int i=0; i<grid.length; i++){
            for(int j=0; j<grid[0].length; j++){
                if(grid[i][j]=='W'){
                    continue;
                }
                if(i==0 || grid[i-1][j]=='W'){
                    col[j] = KillColumn(grid, i, j);
                }
                if(j==0 || grid[i][j-1]=='W'){
                    row = KillRow(grid[i], j);
                }
                if(grid[i][j]=='0'){
                    int cur = row+col[j];
                    result = Math.max(result, cur);
                }
            }
        }
        return result;
    }
    private int KillRow(char[] row, int i){
        int num = 0;
        for(int j=i; j<row.length; j++){
            if(row[j]=='W'){
                break;
            }
            if(row[j]=='E'){
                num++;
            }
        }
        return num;
    }
    private int KillColumn(char[][] grid, int i, int j){
        int num = 0;
        while(i<grid.length && grid[i][j]!='W'){
            if(grid[i][j]=='E'){
                num++;
            }
            i++;
        }
        return num;
    }
}
