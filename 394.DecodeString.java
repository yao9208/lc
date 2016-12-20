public class Solution {
    public String decodeString(String s) {
        String res = "";
        Deque<Integer> num = new LinkedList<>();
        Deque<String> strs = new LinkedList<>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(Character.isDigit(c)){
                int tmp = 0;
                while(i<s.length() && Character.isDigit(s.charAt(i))){
                    tmp = tmp*10 + (s.charAt(i++)-'0');
                }
                num.push(tmp);
            }
            if(s.charAt(i)=='['){
                strs.push(res);
                res = "";
            }else if(s.charAt(i)==']'){
                int repeat = num.pop();
                StringBuilder b = new StringBuilder(strs.pop());
                for(int j=0; j<repeat; j++){
                    b.append(res);
                }
                res = b.toString();
            }else{
                res += s.charAt(i);
            }
        }
        return res;
    }
}
