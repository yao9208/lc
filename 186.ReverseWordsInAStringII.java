public class Solution {
    public void reverseWords(char[] s) {
        int n = s.length;
        reverse(s, 0, n-1);
        int start = 0;
        for(int i=0; i<n; i++){
            if (s[i]==' '){
                reverse(s, start, i-1);
                start = i+1;
            }
        }
        reverse(s, start, n-1);
    }
    public void reverse(char[] s, int start, int end){
        while(start<end){
            char tmp = s[start];
            s[start] = s[end];
            s[end] = tmp;
            start++;
            end--;
        }
    }
}
