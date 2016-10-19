public class Solution {
    public int divide(int dividend, int divisor) {
        if(divisor==1){
            return dividend;
        }
        if (divisor==0 || dividend==Integer.MIN_VALUE && divisor==-1){
            return Integer.MAX_VALUE;
        }
        boolean flag= false;
        if((divisor^dividend)<0){
            flag = true;
        }
        long d = Math.abs((long)dividend);
        long m = Math.abs((long)divisor);
        if (d==0){
            return 0;
        }
        int result = 0;
        while(d>=m){
            long cur = m, tmp = 1;
            while ((cur<<1)<d){
                cur<<=1;
                tmp<<=1;
            }
            result += tmp;
            d-=cur;
        }
        return flag? -(int)result:(int)result;
    }
}
