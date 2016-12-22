public class Solution {
    public boolean makesquare(int[] nums) {
        if (nums == null || nums.length < 4) return false;
        int sum = 0;
        for (int num : nums) sum += num;
        if (sum % 4 != 0) return false;
        Arrays.sort(nums);
        reverse(nums);
        return dfs(nums, new int[4], 0, sum/4);
    }
    private boolean dfs(int[] nums, int[] sums, int start, int len){
        if(start==nums.length && sums[0]==len && sums[1]==len && sums[2]==len){
            return true;
        }
        for(int i=0; i<4; i++){
            if(sums[i]+nums[start]>len){
                continue;
            }
            sums[i]+=nums[start];
            if(dfs(nums, sums, start+1, len)){
                return true;
            }
            sums[i]-=nums[start];
        }
        return false;
    }
    private void reverse(int[] nums) {
        int i = 0, j = nums.length - 1;
        while (i < j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++; j--;
        }
    }
}
