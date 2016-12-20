public class Solution {
    public boolean isNumber(String s) {
        s = s.trim();
        if(s.length()==0){
            return false;
        }
        int i=0;
        if(s.charAt(i)=='+'||s.charAt(i)=='-'){
            i++;
        }
        int pt = 0, num = 0;
        while(i<s.length() && (Character.isDigit(s.charAt(i)) || s.charAt(i)=='.')){
            if(s.charAt(i)=='.'){
                pt++;
            }else{
                num++;
            }
            i++;
        }
        if(num==0 || pt>1){
            return false;
        }
        num=0;
        if(i<s.length() && s.charAt(i)=='e'){
            i++;
            if(i<s.length() && (s.charAt(i)=='+'||s.charAt(i)=='-')){
                i++;
            }
            while(i<s.length() && Character.isDigit(s.charAt(i))){
                i++;
                num++;
            }
            if(num<1){
                return false;
            }
        }
        return i==s.length();
    }
}
