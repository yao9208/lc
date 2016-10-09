public class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder b = new StringBuilder();
        int i = num1.length()-1, j = num2.length()-1;
        int carry = 0;
        while (i>=0 || j>=0){
            int n1 = i<0 ? 0:(int)(num1.charAt(i)-'0');
            int n2 = j<0 ? 0:(int)(num2.charAt(j)-'0');
            int cur = n1+n2+carry;
            carry = cur/10;
            b.append((char)('0'+cur%10));
            i--;
            j--;
        }
        if(carry==1){
            b.append('1');
        }
        return b.reverse().toString();
    }
}
