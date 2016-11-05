public class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if(n==0){
            return 0;
        }
        int[] sell = new int[n];
        int[] buy = new int[n];
        buy[0] = -prices[0];
        int result = 0;
        for(int i=1; i<n; i++){
            sell[i] = Math.max(buy[i-1]+prices[i], sell[i-1]+prices[i]-prices[i-1]);
            if(i>1){
                buy[i] = Math.max(sell[i-2]-prices[i], buy[i-1]+prices[i-1]-prices[i]);
            }else{
                buy[i] = buy[i-1]+prices[i-1]-prices[i];
            }
            result = Math.max(result, sell[i]);
        }
        return result;
    }
}

//http://bookshadow.com/weblog/2015/11/24/leetcode-best-time-to-buy-and-sell-stock-with-cooldown/
