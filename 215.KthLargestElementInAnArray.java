public class Solution {
    public int findKthLargest(int[] nums, int k) {
        k = nums.length-k;
        int left = 0, right = nums.length-1;
        while (left<right){
            int i = partition(nums, left, right);
            if(i<k){
                left = i+1;
            }else if(i>k){
                right = i-1;
            }else{
                break;
            }
        }
        return nums[k];
    }
    private int partition(int[] nums,  int start, int end){
        if(start==end){
            return start;
        }
        int pivot = nums[end];
        int i = start, j = end-1;
        while (i<=j){
            if(nums[i]<pivot){
                i++;
            }else if(nums[j]>=pivot){
                j--;
            }else{
                swap(nums, i, j);
            }
        }
        swap(nums, i, end);
        return i;
    }
    private void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
