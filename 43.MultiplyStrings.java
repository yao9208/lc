public class Solution {
    public String multiply(String num1, String num2) {
        char[] s1 = num1.toCharArray();
        char[] s2 = num2.toCharArray();
        char[] r = new char[s1.length+s2.length];
        for(int i=0; i<r.length; i++){
            r[i]='0';
        }
        for(int i=s1.length-1; i>=0; i--){
            int carry = 0;
            for(int j=s2.length-1; j>=0; j--){
                int tmp = (r[1+j+i]-'0')+(s1[i]-'0')*(s2[j]-'0')+carry;
                r[i+j+1] = (char)(tmp%10+'0');
                carry = tmp/10;
            }
            r[i]+=carry;
        }
        int k=0;
        while(r[k]=='0'&&k<r.length-1)k++;
        String result = new String(r);
        return result.substring(k);
    }
}
