public class Solution {
    public int maximumGap(int[] nums) {
        if (nums == null || nums.length < 2)
            return 0;
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for(int n:nums){
            if(n<min){
                min = n;
            }
            if(n>max){
                max = n;
            }
        }
        if (max==min){
            return 0;
        }
        int gap = (int)Math.ceil((double)(max-min)/(nums.length-1));
        int[] bucketsMIN = new int[nums.length - 1]; // store the min value in that bucket
        int[] bucketsMAX = new int[nums.length - 1]; // store the max value in that bucket
        Arrays.fill(bucketsMIN, Integer.MAX_VALUE);
        Arrays.fill(bucketsMAX, Integer.MIN_VALUE);
        for(int i=0; i<nums.length; i++){
            int idx = (nums[i]-min)/gap;
            if(nums[i]==max){
                idx = nums.length-2;
            }
            if(nums[i]<bucketsMIN[idx]){
                bucketsMIN[idx] = nums[i];
            }
            if(nums[i]>bucketsMAX[idx]){
                bucketsMAX[idx] = nums[i];
            }
        }
        int prevmax = bucketsMAX[0];
        int result = 0;
        for(int i=1; i<nums.length-1; i++){
            int curmin = bucketsMIN[i];
            if(curmin==Integer.MAX_VALUE){
                continue;
            }
            result = Math.max(result, curmin-prevmax);
            prevmax = bucketsMAX[i];
        }
        return Math.max(gap,result);
    }
}
