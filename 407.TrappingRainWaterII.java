public class Solution {
    public int trapRainWater(int[][] heightMap) {
        int result = 0;
        Queue<Cell> q = new PriorityQueue<>();
        if (heightMap.length==0){
            return 0;
        }
        int m = heightMap.length, n = heightMap[0].length;
        boolean[][] visited = new boolean[m][n];
        for(int i=0; i<n; i++){
            q.offer(new Cell(0, i, heightMap[0][i]));
            q.offer(new Cell( m-1, i,heightMap[m-1][i]));
            visited[0][i]=true;
            visited[m-1][i]=true;
        }
        for(int i=1; i<m-1; i++){
            q.offer(new Cell(i, 0,heightMap[i][0]));
            q.offer(new Cell(i, n-1, heightMap[i][n-1]));
            visited[i][0]=true;
            visited[i][n-1]=true;
        }
        int[][] dir = new int[][]{{0,1}, {0, -1}, {1,0}, {-1, 0}};

        while (!q.isEmpty()){
            Cell cur = q.poll();
            for(int i=0; i<4; i++){
                int x = cur.x+dir[i][0], y = cur.y+dir[i][1];
                if(x>=0 && x<m && y>=0 && y<n && !visited[x][y]){
                    Cell next = new Cell(x, y, Math.max(cur.val, heightMap[x][y]));
                    visited[x][y]=true;
                    result += Math.max(0, cur.val-heightMap[x][y]);
                    q.offer(next);
                }
            }
        }
        return result;
    }
    class Cell implements Comparable<Cell>{
        int val;
        int x, y;
        public Cell(int x, int y, int val){
            this.x = x;
            this.y = y;
            this.val = val;
        }
        public int compareTo(Cell that){
            return this.val-that.val;
        }
    }
}
