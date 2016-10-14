public class Solution {
    public boolean increasingTriplet(int[] nums) {
        Integer F=null, S=null, T=null;
        for (int n:nums){
          if(F==null || n<=F){
            F = n;
          }else if(S==null || n<=S){
            S = n;
          }else if(T==null || n<=T){
            T = n;
          }
        }
        return T!=null;
    }
}
