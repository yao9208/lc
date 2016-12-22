public class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        int result = 0;
        Arrays.sort(heaters);
        for(int h:houses){
            int dis = minDistance(houses, heaters, h);
            result = Math.max(result, dis);
        }
        return result;
    }
    private int minDistance(int[] house, int[] heaters, int h){
        int i = 0, j = heaters.length-1;
        int result = Integer.MAX_VALUE;
        while(i<=j){
            int mid = i+(j-i)/2;
            if(heaters[mid]==h){
                return 0;
            }else if(heaters[mid]>h){
                j = mid-1;
            }else{
                i = mid+1;
            }
            result = Math.min(result, Math.abs(h-heaters[mid]));
        }
        return result;
    }
}
