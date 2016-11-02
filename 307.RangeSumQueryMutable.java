public class NumArray {
    int[] tree;
    int n;
    public NumArray(int[] nums) {
        n = nums.length;
        tree = new int[2*n];
        for(int i=n; i<2*n; i++){
            tree[i] = nums[i-n];
        }
        for(int i=n-1; i>0; i--){
            tree[i] = tree[2*i]+tree[2*i+1];
        }
    }

    void update(int i, int val) {
        int pos = i+n;
        tree[pos] = val;
        while(pos>0){
            int left = pos, right = pos;
            if(pos%2==1){
                left = pos-1;
            }else{
                right = pos+1;
            }
            tree[pos/2] = tree[left]+tree[right];
            pos/=2;
        }
    }

    public int sumRange(int i, int j) {
        int l = i+n, r = j+n;
        int sum=0;
        while(l<=r){
            if(l%2==1){
                sum+=tree[l];
                l++;
            }
            if(r%2==0){
                sum+=tree[r];
                r--;
            }
            l/=2;
            r/=2;
        }
        return sum;
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.update(1, 10);
// numArray.sumRange(1, 2);
