public class MedianFinder {

    PriorityQueue <Long> small = new PriorityQueue(),
                         large = new PriorityQueue();
    // Adds a number into the data structure.
    public void addNum(int num) {
        large.offer((long)num);
        small.offer(-large.poll());
        if (small.size()>large.size()){
            large.offer(-small.poll());
        }
    }

    // Returns the median of current data stream
    public double findMedian() {
        if (large.size()>small.size()){
            return large.peek();
        }
        return (large.peek()-small.peek())/2.0;
    }
};

// Your MedianFinder object will be instantiated and called as such:
// MedianFinder mf = new MedianFinder();
// mf.addNum(1);
// mf.findMedian();
