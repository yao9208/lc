public class Solution {
    public String reverseWords(String s) {
        char[] cs = s.trim().toCharArray();
        int n= cs.length;
        if(n<=1){
            return s.trim();
        }
        reverse(cs, 0, n-1);
        int start = 0, end = 1;
        for(int i=1; i<n; i++){
            if(cs[i]==' '&&cs[i-1]!=' '){
                cs[end++] = ' ';
                reverse(cs, start, end-2);

                start = end;
            }else if(cs[i]!=' '){
                cs[end++] = cs[i];
            }
        }
        reverse(cs, start, end-1);
        return (new String(cs)).substring(0, end);
    }
    private void reverse(char[] s, int start, int end){
        while(start<end){
            char tmp= s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }
}
