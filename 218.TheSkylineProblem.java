public class Solution {
    public List<int[]> getSkyline(int[][] buildings) {
        List<int[]> points = new ArrayList<>();
        List<int[]> result = new ArrayList<>();
        for(int[] b:buildings){
            points.add(new int[]{b[0], -b[2]});
            points.add(new int[]{b[1], b[2]});
        }
        Collections.sort(points, (x, y)->{
            if(x[0]!=y[0]){
                return x[0]-y[0];
            }else{
                return x[1]-y[1];
            }
        });
        Queue<Integer> q = new PriorityQueue<>((a, b)->(b-a));
        q.offer(0);
        int prev = 0;
        for(int[] p:points){
            if(p[1]<0){
                q.offer(-p[1]);
            }else{
                q.remove(p[1]);
            }
            int cur = q.peek();
            if(cur!=prev){
                result.add(new int[]{p[0], cur});
                prev = cur;
            }
        }
        return result;
    }
}
