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
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root==null){
            return null;
        }
        if(root.val>key){
            root.left = deleteNode(root.left, key);
        }else if(root.val<key){
            root.right = deleteNode(root.right, key);
        }else{
            if(root.left==null || root.right==null){
                return root.left==null? root.right:root.left;
            }else{
                int max = largest(root.left);
                root.val = max;
                root.left = deleteNode(root.left, max);
            }
        }

        return root;
    }
    private int largest(TreeNode root){
        int max = root.val;
        while(root!=null){
            max = Math.max(max, root.val);
            root = root.right;
        }
        return max;
    }
}
