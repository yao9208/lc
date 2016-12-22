public class Solution {
    public int totalHammingDistance(int[] nums) {
        int result = 0;
        int[] countOne = new int[31];
        for(int i=0; i<nums.length; i++){
            for(int j=0; j<31; j++){
                countOne[j] += (nums[i]>>j)&1;
            }
        }
        for(int i=0; i<31; i++){
            result += countOne[i]*(nums.length-countOne[i]);
        }
        return result;
    }
}
