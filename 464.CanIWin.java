public class Solution {
    Map<Integer, Boolean> map;
    boolean[] used;
    public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
        int sum = (1+maxChoosableInteger)*maxChoosableInteger/2;
        if(sum < desiredTotal) return false;
        if(desiredTotal <= 0) return true;
        used = new boolean[maxChoosableInteger+1];
        map = new HashMap<>();
        return win(desiredTotal);
    }
    private boolean win(int total) {
        if(total<=0){
            return false;
        }
        int key = format(used);
        if(map.containsKey(key)){
            return map.get(key);
        }
        for(int i=1; i<used.length; i++){
            if(!used[i]){
                used[i] = true;
                if(!win(total-i)){
                    map.put(key, true);
                    used[i]=false;
                    return true;
                }
                used[i] = false;
            }
        }
        map.put(key, false);
        return false;
    }
    private Integer format(boolean[] status){
        Integer result = 0;
        for(int i=0; i<status.length; i++){
            if(status[i]){
                result |= (1<<i);
            }
        }
        return result;
    }
}
