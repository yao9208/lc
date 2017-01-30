public class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        int[][] dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
        List<Integer> result = new ArrayList<>();
        int[] p = new int[m*n];
        Arrays.fill(p, -1);
        int count = 0;
        for(int[] position:positions){
            int x = position[0], y = position[1];
            int root = x*n+y;
            p[root] = root;
            count++;
            for(int[] dir:dirs){
                int nx = x+dir[0];
                int ny = y+dir[1];
                if(nx>=0 && nx<m && ny>=0 && ny<n){
                    if(p[nx*n+ny]==-1) continue;
                    int newroot = find(nx*n+ny, p);
                    if(root!=newroot){
                        p[root] = newroot;
                        root = newroot;
                        count--;
                    }
                }
            }
            result.add(count);
        }
        return result;
    }
    private int find(int point, int[] p){
        while(p[point]!=point){
            p[point] = p[p[point]];
            point = p[point];
        }
        return point;
    }
}
