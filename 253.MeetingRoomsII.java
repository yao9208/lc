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
    class intervalComparator implements Comparator<Interval>{
    public int compare(Interval o1, Interval o2){
        if(o1.start!=o2.start){
            return o1.start-o2.start;
        }
        return o1.end - o2.end;
    }
}
public int minMeetingRooms(Interval[] intervals) {
    if(intervals==null || intervals.length==0){
        return 0;
    }
    Arrays.sort(intervals, new intervalComparator());
    Queue<Interval> q = new PriorityQueue<Interval>((a, b)->(a.end-b.end));
    q.offer(intervals[0]);
    for(int i=1; i<intervals.length; i++){
        Interval cur = q.poll();
        if(intervals[i].start>=cur.end){
            cur.end = intervals[i].end;
        }else{
            q.offer(intervals[i]);
        }
        q.offer(cur);
    }
    return q.size();
}
}
