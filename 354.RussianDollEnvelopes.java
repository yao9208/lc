public class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        Queue<Tuple> queue = new PriorityQueue<Tuple>();
        if (envelopes.length==0){
            return 0;
        }
        for (int[] envelope:envelopes){
            queue.offer(new Tuple(envelope[0], envelope[1]));
        }
        int[] dp = new int[envelopes.length];
        Tuple[] e = new Tuple[envelopes.length];
        for (int i=0; i<envelopes.length; i++){
            e[i] = queue.poll();
        }
        int result = 1;
        for (int i=0; i<e.length; i++){
            dp[i] = 1;
            for (int j=i-1; j>=0; j--){
                if (e[i].w>e[j].w && e[i].h>e[j].h){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
            result = Math.max(result, dp[i]);
        }
        return result;
    }
    class Tuple implements Comparable<Tuple>{
        int w;
        int h;
        public Tuple(int w, int h){
            this.w = w;
            this.h = h;
        }
        public int compareTo(Tuple that){
            if (this.w!=that.w){
                return this.w-that.w;
            }else if (this.h!=that.h){
                return this.h-that.h;
            }
            return 0;
        }
    }
}
