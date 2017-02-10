public class Solution {
    public int longestPalindromeSubseq(String s) {
        int n = s.length();
        int[][] dp = new int[n][n];
        for(int i=0; i<n;  i++){
            dp[i][i] = 1;
        }
        for(int k=1; k<n; k++){
            for(int i=0;i<n-k; i++){
                if(s.charAt(i)!=s.charAt(i+k)){
                    dp[i][i+k] = Math.max(dp[i][i+k-1], dp[i+1][i+k]);
                }else{
                    //if(k==1) dp[i][i+k]=2;
                    dp[i][i+k] = dp[i+1][i+k-1]+2;
                }
            }
        }
        return dp[0][n-1];
    }
}
