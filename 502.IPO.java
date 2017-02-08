public class Solution {
    public int findMaximizedCapital(int k, int W, int[] Profits, int[] Capital) {
        Queue<int[]> cap = new PriorityQueue<>((a, b)->(a[0]-b[0]));
        Queue<int[]> pro = new PriorityQueue<>((a,b)->(b[1]-a[1]));

        int n = Profits.length;
        for(int i=0; i<n; i++){
            cap.offer(new int[]{Capital[i], Profits[i]});
        }
        for(int i=0; i<k; i++){
            while(!cap.isEmpty() && cap.peek()[0]<=W){
                pro.offer(cap.poll());
            }
            if(pro.isEmpty()){
                break;
            }
            W += pro.poll()[1];
        }
        return W;
    }
}
