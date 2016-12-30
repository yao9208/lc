public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        Map<Integer, Integer>[] map = new Map[A.length];
        int result = 0;
        for(int i=0; i<A.length; i++){
            map[i] = new HashMap<>();
            for(int j=0; j<i; j++){
                if((long)A[i]-A[j]>Integer.MAX_VALUE) continue;
                if((long)A[i]-A[j]<Integer.MIN_VALUE) continue;
                int diff = A[i]-A[j];
                int count = map[j].getOrDefault(diff, 0);
                map[i].put(diff, map[i].getOrDefault(diff, 0)+count+1);
                result += count;
            }
        }
        return result;
    }
}
