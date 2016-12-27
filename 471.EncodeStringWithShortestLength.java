public class Solution {
    public String encode(String s) {
        int n = s.length();
        String[][] dp = new String[n][n];
        for(int l = 0; l<n; l++){
            for(int i=0; i<n-l; i++){
                int j = i+l;
                String sub = s.substring(i, j+1);
                dp[i][j] = sub;
                if(l<4){
                    continue;
                }
                for(int k=i; k<j; k++){
                    if(dp[i][k].length()+dp[k+1][j].length()<dp[i][j].length()){
                        dp[i][j] = dp[i][k] + dp[k+1][j];
                    }
                }
                for(int k=0; k<sub.length(); k++){
                    String repeat = sub.substring(0, k+1);
                    if(repeat!=null && (l+1)%repeat.length()==0 && sub.replaceAll(repeat, "").length()==0){
                        String encode = (l+1)/repeat.length()+"["+dp[i][i+k]+"]";
                        if(encode.length()<dp[i][j].length()){
                            dp[i][j] = encode;
                        }
                    }
                }
            }
        }
        return dp[0][n-1];
    }
}
