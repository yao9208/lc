public class Solution {
    public int minMoves(int[] nums) {
        int min = Integer.MAX_VALUE;
        for(int n:nums){
            min = Math.min(min, n);
        }
        int result = 0;
        for(int n:nums){
            result += (n-min);
        }
        return result;
    }
}
