public class Solution {
    public int hammingDistance(int x, int y) {
        int xor = x^y;
        int result = 0;
        for(int i=0; i<31; i++){
            result += (xor>>i)&1;
        }
        return result;
    }
}
