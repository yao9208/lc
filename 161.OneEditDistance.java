public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        if (s.length()>t.length()){
            return isOneEditDistance(t, s);
        }
        int m = s.length(), n = t.length();
        if(n-m>1){
            return false;
        }
        int i=0, j=0;
        for(; i<m && j<n && s.charAt(i)==t.charAt(j); i++, j++);
        if (i==m){
            return (n-m)==1;
        }
        if(n-m==0)
            i++;
        j++;
        for(;i<m && j<n && s.charAt(i)==t.charAt(j); i++, j++);
        if(i==m && j==n){
            return true;
        }else{
            return false;
        }
    }
}
