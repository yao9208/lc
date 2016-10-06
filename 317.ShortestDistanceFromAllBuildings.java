public class Solution {
    public int shortestDistance(int[][] grid) {
        if(grid.length==0){
            return -1;
        }
        int m = grid.length, n = grid[0].length;
        int[][] dis = new int[m][n];
        int[][] reach = new int[m][n];
        int buildings = 0;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j]==1){
                    buildings ++;
                    bfs(grid, dis, reach, i, j);
                }
            }
        }
        int mindis = Integer.MAX_VALUE;
        for(int i=0; i<m; i++){
            for(int j=0; j<n; j++){
                if(grid[i][j]==0 && reach[i][j]==buildings){
                    mindis = Math.min(mindis, dis[i][j]);
                }
            }
        }
        return mindis==Integer.MAX_VALUE? -1:mindis;
    }
    private void bfs(int[][] grid, int[][] dis, int[][] reach, int x, int y){
        int m = grid.length, n = grid[0].length;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> q = new ArrayDeque<>();
        int[][] dir = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
        q.offer(new int[]{x, y});
        int level = 0;
        while(!q.isEmpty()){
            int size = q.size();
            for(int p = 0; p<size; p++){
                int[] cur = q.poll();
                int i = cur[0], j = cur[1];
                if(visited[i][j]){
                    continue;
                }
                dis[i][j] += level;
                visited[i][j] = true;
                reach[i][j] += 1;
                for(int k=0; k<4; k++){
                    int nextx = i+dir[k][0];
                    int nexty = j+dir[k][1];
                    if(nextx>=0 && nextx<m && nexty>=0 && nexty<n && grid[nextx][nexty]==0 && !visited[nextx][nexty]){
                        q.offer(new int[]{nextx, nexty});
                    }
                }
            }
            level++;
        }
    }
}
