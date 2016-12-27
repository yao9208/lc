public class Solution {
    public boolean isConvex(List<List<Integer>> points) {
        long last = 0;
        int n = points.size();
        for(int i=2; i<points.size()+3; i++){
            List<Integer> p0 = points.get((i-2)%n), p1 = points.get((i-1)%n), p2 = points.get(i%n);
            long tmp = (p1.get(0)-p0.get(0))*(p2.get(1)-p0.get(1))-(p2.get(0)-p0.get(0))*(p1.get(1)-p0.get(1));
            if(tmp!=0){
                if(last*tmp<0){
                    return false;
                }
                last = tmp;
            }
        }
        return true;
    }
}
