public class Solution {
    class Point {
        int x,y,dis;
        String path;
        public Point(int x, int y, int dis, String path){
            this.x = x;this.y = y;this.dis = dis;
            this.path = path;
        }
    }
    public String findShortestWay(int[][] maze, int[] start, int[] destination) {
        int m=maze.length, n=maze[0].length;
        String result = "impossible";
        int reslen = Integer.MAX_VALUE;
        Queue<Point> queue= new PriorityQueue<>((x, y)->x.dis-y.dis);
        int[][] dirs= {{-1,0},{0,1},{1,0},{0,-1}};
        String[] pdir = {"u","r","d","l"};
        int[][] len = new int[m][n];
        for(int i=0; i<m; i++){
            Arrays.fill(len[i], Integer.MAX_VALUE);
        }
        queue.offer(new Point(start[0], start[1], 0, ""));
        len[start[0]][start[1]]=0;
        while(!queue.isEmpty()){
            Point p = queue.poll();
            int x = p.x, y = p.y, cur = p.dis;
            String curpath = p.path;
            for(int k = 0; k<4; k++){
                int[] tmp = roll(maze, x, y, dirs[k], destination);
                if(tmp[2]>0 && len[tmp[0]][tmp[1]]>=cur+tmp[2]){
                    if(tmp[0]==destination[0] && tmp[1]==destination[1]){
                        if(reslen == cur+tmp[2]){
                            if((curpath+pdir[k]).compareTo(result)<0){
                                result = curpath+pdir[k];
                            }
                        }else{
                            reslen=cur+tmp[2];
                            result = curpath+pdir[k];
                        }
                    }
                    queue.offer(new Point(tmp[0], tmp[1], cur+tmp[2], curpath+pdir[k]));
                    len[tmp[0]][tmp[1]]=cur+tmp[2];
                }
            }
        }
        return result;
    }
    private int[] roll(int[][] maze, int x, int y, int[] dir, int[] hole){
        int step = 0;
        while(canRoll(maze, x, y, dir)){
            step++;
            x += dir[0];
            y += dir[1];
            if(x==hole[0] && y==hole[1]){
                break;
            }
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
