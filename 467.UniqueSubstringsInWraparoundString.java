public class Solution {
    public int findSubstringInWraproundString(String p) {
        if(p.length()==0){
            return 0;
        }
        Map<Character, Integer> map = new HashMap<>();
        int prev = -1;
        int count = 0, result = 0;
        for(int i=0; i<p.length(); i++){
            int cur = p.charAt(i)-'a';
            if(cur == (prev+1)%26){
                count++;
            }else{
                count=1;
            }
            check(p.charAt(i), count, map);
            prev = cur;
        }
        for(int n:map.values()){
            result += n;
        }
        return result;
    }
    private void check(char c, int len, Map<Character, Integer> map){
        if(!map.containsKey(c)){
            map.put(c, len);
        }else{
            map.put(c, Math.max(len, map.get(c)));
        }
    }
}
