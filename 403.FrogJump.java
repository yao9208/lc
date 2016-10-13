public class Solution {
    public boolean canCross(int[] stones) {
        if (stones.length == 0) {
        	return true;
        }
        HashMap<Integer, HashSet<Integer>> map = new HashMap<>();
        for(int s:stones){
            map.put(s, new HashSet<>());
        }
        map.get(0).add(1);
        for(int i=0; i<stones.length; i++){
            int stone = stones[i];
            for(int step:map.get(stone)){
                int reach = stone+step;
                if(reach==stones[stones.length-1]){
                    return true;
                }
                HashSet<Integer> set = map.get(reach);
                if(set!=null){
                    set.add(step);
                    if(step>1) set.add(step-1);
                    set.add(step+1);
                }
            }
        }
        return false;
    }
}
