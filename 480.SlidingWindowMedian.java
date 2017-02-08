public class Solution {
    Queue<Integer> minHeap = new PriorityQueue<>();
    Queue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
    public double[] medianSlidingWindow(int[] nums, int k) {
        int n = nums.length;
        double[] result = new double[n-k+1];

        for(int i=0; i<=n; i++){
            if(i>=k){
                result[i-k] = getMedian();
                remove(nums[i-k]);
            }
            if(i<n){
                add(nums[i]);
            }
        }
        return result;
    }
    private void add(int n){
        if(n<getMedian()){
            maxHeap.offer(n);
        }else{
            minHeap.offer(n);
        }
        adjust();
    }
    private void remove(int n){
        if(n<getMedian()){
            maxHeap.remove(n);
        }else{
            minHeap.remove(n);
        }
        adjust();
    }
    private void adjust(){
        if(maxHeap.size()>minHeap.size()){
            minHeap.offer(maxHeap.poll());
        }
        if(minHeap.size()-1>maxHeap.size()){
            maxHeap.offer(minHeap.poll());
        }
    }
    private double getMedian(){
        if(minHeap.isEmpty() && maxHeap.isEmpty()){
            return 0;
        }
        if(minHeap.size()==maxHeap.size()){
            return ((double)minHeap.peek()+(double)maxHeap.peek())/2.0;
        }else{
            return (double)minHeap.peek();
        }
    }
}
