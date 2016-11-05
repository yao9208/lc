public class Solution {
    public boolean validUtf8(int[] data) {
        int i=0, n = data.length;
        while(i<n){
            int cur = ones(data[i]);
            if(cur>=2){
                for(int j=1; j<cur; j++){
                    if(i+j>=n) return false;
                    if(ones(data[i+j])!=1) return false;
                }
                i+=cur;
            }else if(cur==1){
                return false;
            }else{
                i++;
            }
        }
        return true;
    }
    private int ones(int num){
        int count = 0;
        for(int i=7; i>=0; i--){
            if((num>>i&1)==0){
                break;
            }
            count++;
        }
        return count;
    }
}
