public class Solution {
    public String toHex(int num) {
        if(num==0){
            return "0";
        }
        char[] sign = new char[16];
        for(int i=0; i<10; i++){
            sign[i] = (char)('0'+i);
        }
        for(int i=0;i<6; i++){
            sign[i+10] = (char)('a'+i);
        }
        StringBuilder b = new StringBuilder();
        while(num!=0){
            int remainder = num&15;
            b.append(sign[remainder]);
            num >>>=4;
        }
        return b.reverse().toString();
    }
}
