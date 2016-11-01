public class Solution {
    public int arrangeCoins(int n) {
        long start = 0, end = n;
        while(start<end){
            long mid = start+(end-start)/2+1;
            if(mid*(mid+1)/2>n){
                end = mid-1;
            }else{
                start = mid;
            }
        }
        return (int)start;
    }
}
