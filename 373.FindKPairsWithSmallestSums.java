public class Solution {
    public List<int[]> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<int[]> result = new ArrayList<>();
        if(nums1==null || nums2==null||nums1.length<1 || nums2.length<1||k==0){
            return result;
        }

        Queue<Pair> q = new PriorityQueue<>();
        q.offer(new Pair(0, 0, nums1[0], nums2[0]));
        int l1 = nums1.length, l2 = nums2.length;
        boolean[][] visited = new boolean[l1][l2];
        visited[0][0] = true;
        for (int i = 0; i<k; i++){
            Pair top = q.poll();
            if(top==null){
                break;
            }
            result.add(new int[]{top.m, top.n});
            int x = top.x, y = top.y;

            if(x+1<l1 && !visited[x+1][y]){
                q.offer(new Pair(x+1, y, nums1[x+1], nums2[y]));
                visited[x+1][y] = true;
            }
            if(y+1<l2 && !visited[x][y+1]){
                q.offer(new Pair(x, y+1, nums1[x], nums2[y+1]));
                visited[x][y+1] = true;
            }
        }
        return result;
    }
    class Pair implements Comparable<Pair>{
        int x, y;
        int m, n;
        int sum;
        public Pair(int x, int y, int m, int n){
            this.x = x;
            this.y = y;
            this.m = m;
            this.n = n;
            this.sum = m+n;
        }
        public int compareTo(Pair that){
            return this.sum-that.sum;
        }
    }
}


//https://discuss.leetcode.com/topic/50885/simple-java-o-klogk-solution-with-explanation
