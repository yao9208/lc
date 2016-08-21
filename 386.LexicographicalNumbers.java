public class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<Integer> result = new ArrayList<Integer>();
        helper(result, 0, n);
        return result;
    }
    private void helper(List<Integer> result, int cur, int n){
        if(cur<=n){
            if(cur!=0){
                result.add(cur);
            }
        }else{
            return;
        }
        for (int i=0; i<10; i++){
            int next = cur*10+i;
            if (next!=0){
                helper(result, next, n);
            }
        }
    }
}
