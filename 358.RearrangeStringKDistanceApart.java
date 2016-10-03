public class Solution {
    public String rearrangeString(String str, int k) {
        int[] count = new int[26];
        int[] valid = new int[26];
        for(int i=0; i<str.length(); i++){
            count[str.charAt(i)-'a']++;
        }
        StringBuilder b = new StringBuilder();
        for(int i=0; i<str.length(); i++){
            int pos = findValidCh(count, valid, i);
            if(pos==-1){
                return "";
            }
            b.append((char)('a'+pos));
            count[pos]--;
            valid[pos]+=k;
        }
        return b.toString();
    }
    private int findValidCh(int[] count, int[] valid, int index){
        int pos = -1;
        int maxCount = Integer.MIN_VALUE;
        for(int i=0; i<26; i++){
            if(count[i]>0 && count[i]>maxCount && valid[i]<=index){
                maxCount = count[i];
                pos = i;
            }
        }
        return pos;
    }
}
