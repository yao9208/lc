public class Solution {
    public int countDigitOne(int n) {
        int p = n, x = 1;
        int result = 0;
        while(p>0){
            int digit = p%10;
            p/=10;
            result += p*x;
            if(digit==1){
                result+=n%x+1;
            }else if(digit>1){
                result += x;
            }
            x*=10;
        }
        return result;
    }
}
