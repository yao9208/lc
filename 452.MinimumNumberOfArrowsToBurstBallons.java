public class Solution {
    public int findMinArrowShots(int[][] points) {
        if(points.length==0){
            return 0;
        }
        Arrays.sort(points, (x, y)->(x[0]-y[0]));
        int count = 0;
        int minEnd = Integer.MAX_VALUE;
        for(int i=0; i<points.length; i++){
            if(points[i][0]>minEnd){
                count++;
                minEnd = points[i][1];
            }else{
                minEnd = Math.min(minEnd, points[i][1]);
            }
        }
        return count+1;
    }
}
