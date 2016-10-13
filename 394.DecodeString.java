public class Solution {
    public String decodeString(String s) {
        Deque<Integer> freq = new LinkedList<>();
        Deque<String> code = new LinkedList<>();
        int i=0;
        if(s.length()==0){
            return s;
        }
        while(i<s.length()){
            char c = s.charAt(i);
            if(c>='0' && c<='9'){
                int f = 0;
                while(i<s.length() && s.charAt(i)>='0' && s.charAt(i)<='9'){
                    f = f*10 + (int)(s.charAt(i)-'0');
                    i++;
                }
                freq.push(f);
            }else if(c>='a' && c<='z'){
                String word = "";
                while(i<s.length() && s.charAt(i)>='a' && s.charAt(i)<='z'){
                    word += s.charAt(i);
                    i++;
                }
                String prev = code.isEmpty()? "":code.pop();
                code.push(prev+word);
            }else if(c==']'){
                String cur = code.pop();
                int f = freq.pop();
                String tmp = make(f, cur);
                String prev = code.isEmpty()? "":code.pop();
                code.push(prev+tmp);
                i++;
            }else{
                code.push("");
                i++;
            }
        }
        return code.pop();
    }
    private String make(int freq, String word){
        StringBuilder b = new StringBuilder();
        for(int i=0; i<freq; i++){
            b.append(word);
        }
        return b.toString();
    }

}
