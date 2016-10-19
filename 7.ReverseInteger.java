public class Solution {
    public int reverse(int x) {
        int a = Integer.MAX_VALUE/10, b = Integer.MAX_VALUE%10;
        boolean flag = false;
        if(x<0){
            flag=true;
            if(-x<0){
                return 0;
            }
            x=-x;
        }
        int num=0;
        while(x>0){
            if(num>a || num==a && x%10>=b){
                return 0;
            }
            num = num*10 +x%10;
            x/=10;
        }
        return (flag)? -num:num;
    }
}
