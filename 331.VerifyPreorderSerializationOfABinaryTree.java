public class Solution {
    public boolean isValidSerialization(String preorder) {
        Deque<String> stack = new LinkedList<>();
        if(preorder==null){
            return false;
        }
        String[] pre = preorder.split(",");
        for(int i=0; i<pre.length; i++){
            String cur = pre[i];
            while(cur.equals("#") && !stack.isEmpty() && stack.peek().equals("#")){
                stack.pop();
                if(stack.isEmpty()){
                    return false;
                }
                stack.pop();
            }
            stack.push(cur);
        }
        return stack.size()==1 && stack.peek().equals("#");
    }
}
