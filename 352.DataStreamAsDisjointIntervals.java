/**
 * Definition for an interval.
 * public class Interval {
 *     int start;
 *     int end;
 *     Interval() { start = 0; end = 0; }
 *     Interval(int s, int e) { start = s; end = e; }
 * }
 */
public class SummaryRanges {
    TreeMap<Integer, Interval> map = new TreeMap<>();

    /** Initialize your data structure here. */
    public SummaryRanges() {

    }

    public void addNum(int val) {
        if (map.containsKey(val)){
            return;
        }
        Integer lower = map.lowerKey(val);
        Integer higher = map.higherKey(val);
        if (lower!=null && higher!=null && map.get(lower).end+1==val && higher==val+1){
            map.get(lower).end = map.get(higher).end;
            map.remove(higher);
        }else if (lower!=null && map.get(lower).end+1>=val) {
            map.get(lower).end = Math.max(map.get(lower).end, val);
        }else if (higher!=null && higher==val+1){
            map.put(val, new Interval(val, map.get(higher).end));
            map.remove(higher);
        }else{
            map.put(val, new Interval(val, val));
        }
    }

    public List<Interval> getIntervals() {
        return new ArrayList<>(map.values());
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(val);
 * List<Interval> param_2 = obj.getIntervals();
 */
