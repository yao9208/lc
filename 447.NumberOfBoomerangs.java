public class Solution {
    public int numberOfBoomerangs(int[][] points) {
        int count = 0;
        for(int i=0; i<points.length; i++){
            Map<Integer, Integer> map = new HashMap<>();
            for(int j=0; j<points.length; j++){
                int dis = distance(points[i], points[j]);
                Integer freq = map.get(dis);
                if(freq==null){
                    freq = 0;
                }
                map.put(dis, freq+1);
            }
            for(Map.Entry<Integer, Integer> entry:map.entrySet()){
                int tmp = entry.getValue();
                if(tmp>1){
                    count += tmp*(tmp-1);
                }
            }
        }
        return count;
    }
    private int distance(int[] p1, int[] p2){
        return (p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]);
    }
}
