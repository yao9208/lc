/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    Map<Integer, Integer> map;
    public int[] findFrequentTreeSum(TreeNode root) {
        map = new HashMap<>();
        List<Integer> list = new ArrayList<>();
        int max = 0;
        helper(root);
        for(Map.Entry<Integer, Integer> entry:map.entrySet()){
            int freq = entry.getValue();
            max = Math.max(max, freq);
        }
        for(Map.Entry<Integer, Integer> entry:map.entrySet()){
            if(entry.getValue()==max){
                list.add(entry.getKey());
            }
        }
        int[] res = new int[list.size()];
        for(int i=0; i<list.size(); i++){
            res[i] = list.get(i);
        }
        return res;
    }
    private int helper(TreeNode root){
        if(root==null){
            return 0;
        }
        int left = helper(root.left);
        int right = helper(root.right);
        int sum = left+right+root.val;
        if(!map.containsKey(sum)){
            map.put(sum, 1);
        }else{
            map.put(sum, map.get(sum)+1);
        }
        return sum;
    }
}
