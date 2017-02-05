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
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if(p.right!=null){
            p = p.right;
            while(p.left!=null){
                p = p.left;
            }
            return p;
        }
        TreeNode candidate = null;
        while(root!=p){
            if(p.val>root.val){
                root = root.right;
            }else{
                candidate = root;
                root = candidate.left;
            }
        }
        return candidate;
    }
}
