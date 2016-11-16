public class Solution {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        int p = 0, q = 0;
        int count = 0;
        while(p<g.length && q<s.length){
            if(s[q]>=g[p]){
                count++;
                p++;
            }
            q++;
        }
        return count;
    }
}
