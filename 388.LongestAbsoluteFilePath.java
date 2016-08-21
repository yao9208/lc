public class Solution {
    public int lengthLongestPath(String input) {
        Stack<Integer> stack = new Stack<Integer>();
        String[] arr = input.split("\n");
        int result = 0;
        int prevlevel = -2;
        int cur = 0;
        for(String s:arr){
            int idx = s.lastIndexOf("\t");
            int tmp = idx;
            while (tmp<=prevlevel) {
                cur -= stack.pop();
                tmp++;
            }
            if (s.contains(".")){
                result = Math.max(result, cur+s.length()-idx);
                prevlevel = idx-1;
            }else{
                cur+=s.length()-idx;
                stack.push(s.length()-idx);
                prevlevel=idx;
            }
        }
        return Math.max(0, result-1);
    }
}
