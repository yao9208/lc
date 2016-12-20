public class Solution {
    public int minMoves2(int[] nums) {
        int result = 0;
        Arrays.sort(nums);
        int i = 0, j = nums.length-1;
        while(i<j){
            result += nums[j--]-nums[i++];
        }
        return result;
    }
}
