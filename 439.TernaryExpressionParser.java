public class Solution {
    public String parseTernary(String expression) {
        Deque<Character> stack = new LinkedList<>();
        int n = expression.length();
        for(int i=n-1; i>=0; i--){
            char c = expression.charAt(i);
            if((c=='T' || c=='F') && i<n-1 && expression.charAt(i+1)=='?' ){
                char a = stack.pop();
                char b = stack.pop();
                stack.push(c=='T'? a:b);
            }else if (c!='?' && c!=':'){
                stack.push(c);
            }
        }
        return Character.toString(stack.peek());
    }
}
