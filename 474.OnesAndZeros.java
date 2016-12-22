public class Solution {
    public int findMaxForm(String[] strs, int m, int n) {
        int[][] dp = new int[m+1][n+1];
        for(String s:strs) {
            int[] res = count(s);
            for(int i=m; i>=res[0]; i--){
                for(int j=n; j>=res[1]; j--){
                    dp[i][j] = Math.max(dp[i][j], 1+dp[i-res[0]][j-res[1]]);
                }
            }
        }
        return dp[m][n];
    }
    private int[] count(String str) {
        int[] result = new int[2];
        for(int i=0; i<str.length(); i++){
            result[str.charAt(i)-'0']++;
        }
        return result;
    }
}
