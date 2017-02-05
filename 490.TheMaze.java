public class Solution {
    public boolean hasPath(int[][] maze, int[] start, int[] destination) {
        int m = maze.length, n = maze[0].length;
        boolean[][] visited = new boolean[m][n];
        int[][] dirs = {{-1,0},{1,0},{0,-1},{0,1}};
        return dfs(maze, start, destination, visited, dirs);
    }
    private boolean dfs(int[][] maze, int[] start, int[] destination, boolean[][] visited, int[][] dirs){
        if(visited[start[0]][start[1]]){
            return false;
        }
        if(Arrays.equals(start, destination)){
            return true;
        }
        visited[start[0]][start[1]] = true;
        for(int[] dir:dirs){
            int[] newstart = roll(maze, start, dir);
            if(dfs(maze, newstart, destination, visited, dirs)){
                return true;
            }
        }
        return false;
    }
    private int[] roll(int[][] maze, int[] start, int[] dir){
        int x = start[0], y = start[1];
        while(canRoll(maze, x, y, dir)){
            x += dir[0];
            y += dir[1];
        }
        return new int[]{x,y};
    }
    private boolean canRoll(int[][] maze, int x, int y, int[] dir){
        int m = maze.length, n = maze[0].length;
        x += dir[0];
        y += dir[1];
        if(x<0 || x>=m || y<0 || y>=n || maze[x][y]!=0) return false;
        return true;
    }
}
