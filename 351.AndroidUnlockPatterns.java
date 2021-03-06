public class Solution {
    public int numberOfPatterns(int m, int n) {
        int[][] skip = new int[10][10];
        skip[1][3] = skip[3][1] = 2;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][7] = skip[7][1] = 4;
        skip[2][8] = skip[8][2] = skip[4][6] = skip[6][4] = skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5;
        boolean[] visited = new boolean[10];
        int result = 0;
        for(int i=m; i<=n; i++){
            result += dfs(i-1, visited, skip, 1)*4;
            result += dfs(i-1, visited, skip, 2)*4;
            result += dfs(i-1, visited, skip, 5);
        }
        return result;
    }
    private int dfs(int remain, boolean[] visited, int[][] skip, int cur){
        if(remain==0){
            return 1;
        }
        visited[cur] = true;
        int result = 0;
        for(int i=1; i<10; i++){
            if(!visited[i] && (skip[cur][i]==0 || visited[skip[cur][i]])){
                result += dfs(remain-1, visited, skip, i);

            }
        }
        visited[cur] = false;
        return result;
    }
}
