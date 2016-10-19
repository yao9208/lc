public class Solution {
    int idx=0;
    int max=0;
    public String longestPalindrome(String s) {
       // int max = 0;
        int n = s.length();
        for(int i=0; i<n; i++){
            maxlen(s, i, 0);
            maxlen(s, i, 1);
        }
        return s.substring(idx, idx+max);
    }
    public int maxlen(String s, int center, int shift){
        int n = s.length()-1;

        int left = center, right = center+shift;
        while(left>=0 && right<=n){
            if(s.charAt(left)==s.charAt(right)){
                if((right-left+1)>max){
                    max = right-left+1;
                    idx = left;
                }
            }else{
                break;
            }
            left--;
            right++;
        }
        return max;
    }
}
