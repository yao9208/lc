public class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        if(n==0){
            return m==0;
        }
        if(n>1 && p.charAt(1)=='*'){
            return (isMatch(s, p.substring(2)) || m>0 && (s.charAt(0)==p.charAt(0)||p.charAt(0)=='.') && isMatch(s.substring(1), p));
        }else{
            return m>0 && (s.charAt(0)==p.charAt(0)||p.charAt(0)=='.') && isMatch(s.substring(1), p.substring(1));
        }
    }
}


public class Solution {
    public boolean isMatch(String ss, String pp) {
        int m = ss.length(), n = pp.length();
        char[] s = ss.toCharArray();
        char[] p = pp.toCharArray();
        boolean[][] dp = new boolean[m+1][n+1];
        dp[0][0] = true;
        for (int i=1; i<=m; i++){
            dp[i][0] = false;
        }
        for(int i=1; i<=n; i++){
            dp[0][i] = i>1 && dp[0][i-2] && p[i-1]=='*';
        }
        for(int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if(p[j]!='*'){
                    dp[i+1][j+1] = dp[i][j] && (p[j]=='.' || s[i]==p[j]);
                }else{
                    dp[i+1][j+1] = (j>0 && dp[i+1][j-1]) || dp[i+1][j] || (j>0 && dp[i][j+1] && (s[i]==p[j-1]||p[j-1]=='.'));
                }
            }
        }
        return dp[m][n];
    }
}
