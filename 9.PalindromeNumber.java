public class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int num = 0;
        int xx=x;
        while(xx>0){
            num = num*10 + xx%10;
            xx/=10;
        }
        return (num==x);
    }
}
