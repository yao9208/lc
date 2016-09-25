public class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int len = 0;
        for (int num:nums){
            int start = 0, end = len;
            while (start<end){
                int mid = start+(end-start)/2;
                if (dp[mid]<num){
                    start = mid+1;
                }else{
                    end = mid;
                }
            }
            dp[start] = num;
            if(start==len){
                len++;
            }
        }
        return len;
    }
}
