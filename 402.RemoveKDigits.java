public class Solution {
    public String removeKdigits(String num, int k) {
        char[] n = num.toCharArray();
        int digits = n.length-k;
        int top = 0;
        for(int i=0; i<n.length; i++){
            while(top>0 && k>0 && n[i]<n[top-1]){
                top--;
                k--;
            }
            n[top++] = n[i];
        }
        int start = 0;
        while(start<digits &&n[start]=='0'){
            start++;
        }
        return start==digits? "0":new String(n, start, digits-start);
    }
}
