public class Solution {
    class Point {
        int x,y,dis;
        public Point(int x, int y, int dis){
            this.x = x;this.y = y;this.dis = dis;
        }
    }
    public int shortestDistance(int[][] maze, int[] start, int[] destination) {
        int m=maze.length, n=maze[0].length;
        Queue<Point> queue= new PriorityQueue<>((x, y)->x.dis-y.dis);
        int[][] dirs= {{-1,0},{0,1},{1,0},{0,-1}};
        int[][] len = new int[m][n];
        for(int i=0; i<m; i++){
            Arrays.fill(len[i], Integer.MAX_VALUE);
        }
        queue.offer(new Point(start[0], start[1], 0));
        len[start[0]][start[1]]=0;
        while(!queue.isEmpty()){
            Point p = queue.poll();
            int x = p.x, y = p.y, cur = p.dis;
            for(int[] d:dirs){
                int[] tmp = roll(maze, x, y, d);
                if(len[tmp[0]][tmp[1]]>cur+tmp[2]){
                    queue.offer(new Point(tmp[0], tmp[1], cur+tmp[2]));
                    len[tmp[0]][tmp[1]]=cur+tmp[2];
                }
            }
        }
        if(len[destination[0]][destination[1]]==Integer.MAX_VALUE){
            return -1;
        }
        return len[destination[0]][destination[1]];
    }
    private int[] roll(int[][] maze, int x, int y, int[] dir){
        int step = 0;
        while(canRoll(maze, x, y, dir)){
            step++;
            x += dir[0];
            y += dir[1];
        }
        return new int[]{x,y,step};
    }
    private boolean canRoll(int[][] maze, int x, int y, int[] dir){
        int m = maze.length, n = maze[0].length;
        x += dir[0];
        y += dir[1];
        if(x<0 || x>=m || y<0 || y>=n || maze[x][y]!=0) return false;
        return true;
    }
}
