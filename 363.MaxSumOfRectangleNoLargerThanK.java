public class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        int result = Integer.MIN_VALUE;
        for(int left = 0; left<n; left++){
            int[] cum = new int[m];
            int res = Integer.MIN_VALUE;
            for(int right = left; right<n; right++){
                for(int r=0; r<m; r++){
                    cum[r] += matrix[r][right];
                }
                res = largestSumNoLargerThanK(cum, k);
                result = Math.max(result, res);
            }
        }
        return result;
    }
    private int largestSumNoLargerThanK(int[] cum, int k){
        int max = Integer.MIN_VALUE;
        TreeSet<Integer> tree = new TreeSet<>();
        tree.add(0);
        int tmp = 0;
        for(int c:cum){
            tmp += c;
            Integer ceiling = tree.ceiling(tmp-k);
            if(ceiling!=null){
                max = Math.max(max, tmp-ceiling);
            }
            tree.add(tmp);
        }
        return max;
    }
}
