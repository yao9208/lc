public class Solution {
    public int thirdMax(int[] nums) {
        Integer first= null, second = null, third = null;
        for(int n:nums){
            if(first!=null && n==first || second!=null && n==second){
                continue;
            }
            if(first==null || n>first){
                third = second;
                second = first;
                first = n;
            }else if(second==null || n>second){
                third = second;
                second = n;
            }else if(third==null || n>third){
                third = n;
            }
        }
        return third==null? first:third;
    }
}
