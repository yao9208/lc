public class Solution {
    public boolean repeatedSubstringPattern(String str) {
        int len = str.length();
        if(len<2){
            return false;
        }
        for(int i=1; i<len; i++){
            if(len%i!=0){
                continue;
            }
            String tmp = str.substring(0, i);
            if(check(str, tmp)){
                return true;
            }
        }
        return false;
    }
    private boolean check(String str, String pattern){
        int len = str.length();
        for(int i=pattern.length(); i<len; i++){
            if(str.charAt(i)!=pattern.charAt(i%pattern.length())){
                return false;
            }
        }
        return true;
    }
}
