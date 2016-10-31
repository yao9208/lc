public class Solution {
    public int calculate(String s) {
        int n = s.length();
        if(n==0){
            return 0;
        }
        int tmp = 0;
        char sign = '+';
        Deque<Integer> stack = new LinkedList<>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(Character.isDigit(c)){
                tmp = 10*tmp+(c-'0');
            }
            if(i==n-1 || !Character.isDigit(c) && c!=' '){
                switch (sign){
                    case '+': stack.push(tmp); break;
                    case '-': stack.push(-tmp); break;
                    case '*': stack.push(stack.pop()*tmp); break;
                    case '/': stack.push(stack.pop()/tmp); break;
                }
                sign = c;
                tmp = 0;
            }
        }
        int result = 0;
        for (int i:stack){
            result += i;
        }
        return result;
    }
}
