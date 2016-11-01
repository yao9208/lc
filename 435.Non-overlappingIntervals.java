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
    public int eraseOverlapIntervals(Interval[] intervals) {
        int count = 0;
        if(intervals.length==0){
            return 0;
        }
        Arrays.sort(intervals, (x, y)->(x.start-y.start));
        int end = intervals[0].end;
        for(int i=1; i<intervals.length; i++){
            if(intervals[i].start>=end){
                end = intervals[i].end;
            }else{
                count++;
                end = Math.min(end, intervals[i].end);
            }
        }
        return count;
    }
}
