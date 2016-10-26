public class NumArray {

    int[] cum;
    public NumArray(int[] nums) {
        cum = new int[nums.length+1];
        for(int i=0; i<nums.length; i++){
            cum[i+1] = cum[i]+nums[i];
        }
    }

    public int sumRange(int i, int j) {
        return cum[j+1]-cum[i];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
