public class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stack = new Stack<>();
        int last = -1;
        int maxlen=0, idx = 0;
        for(int i=0; i<s.length(); i++){
            if(s.charAt(i)=='('){
                stack.push(i);
            }else{
                if(stack.isEmpty()){
                    last = i;
                }else{
                    stack.pop();
                    int curlen = 0;
                    if(!stack.isEmpty()){
                        curlen = i-stack.peek();
                    }else{
                        curlen = i-last;
                    }

                    if(curlen>maxlen){
                        maxlen = curlen;
                    }
                }
            }
        }
        return maxlen;
    }
}
