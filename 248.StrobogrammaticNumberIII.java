public class Solution {
  int count = 0;
    public int strobogrammaticInRange(String low, String high) {
      char[][] pairs = {{'0', '0'}, {'1', '1'}, {'6', '9'}, {'8', '8'}, {'9', '6'}};
      for(int i=low.length(); i<=high.length(); i++){
        dfs(pairs, new char[i], 0, i-1, low, high);
      }
      return count;
    }
    private void dfs(char[][] pairs, char[] str, int left, int right, String low, String high){
      if(left>right){
        String cur = new String(str);
        if (cur.length()==low.length() && cur.compareTo(low)<0 ||
            cur.length()==high.length() && cur.compareTo(high)>0){
          return;
        }
        count++;
        return;
      }
      for(char[] p:pairs){
        str[left] = p[0];
        str[right] = p[1];
        if(str.length!=1 && str[0]=='0') continue;
        if(left<right || left==right && p[0]==p[1]){
          dfs(pairs, str, left+1, right-1, low, high);
        }
      }
    }
}
