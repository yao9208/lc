/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class Solution {
    public int[] findRightInterval(Interval[] intervals) {
        Interval[] copy = new Interval[intervals.length];
        int[] result = new int[intervals.length];
        for(int i=0; i<intervals.length; i++){
            copy[i] = new Interval(intervals[i].start, i);
        }
        Arrays.sort(copy, (x,y)->(x.start-y.start));
        for(int i=0; i<intervals.length; i++){
            int key = intervals[i].end;
            int start = 0, end = intervals.length-1;
            while(start<end){
                int mid = start+(end-start)/2;
                if (copy[mid].start<key){
                    start = mid+1;
                }else{
                    end = mid;
                }
            }
            if(copy[start].start>=key){
                result[i]=copy[start].end;
            }else{
                result[i]=-1;
            }
        }
        return result;
    }
}
