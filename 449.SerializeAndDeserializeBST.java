/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder b = new StringBuilder();
        if(root==null){
          return "";
        }
        b.append(root.val);
        b.append(',');
        b.append(serialize(root.left));
        b.append(serialize(root.right));
        return b.toString();
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        return helper(data, Integer.MIN_VALUE, Integer.MAX_VALUE, new int[1]);
    }
    private TreeNode helper(String data, int lower, int upper, int[] pos){
        if(pos[0]==data.length()){
            return null;
        }
        int num = 0;
        int p = pos[0];
        while(p<data.length() && Character.isDigit(data.charAt(p))){
          num = num*10+(data.charAt(p)-'0');
          p++;
        }
        p++;
        if(p>pos[0] && (num<lower || num>upper)){
          return null;
        }
        TreeNode cur = new TreeNode(num);
        pos[0] = p;
        cur.left = helper(data, lower, num, pos);
        cur.right = helper(data, num, upper,pos);
        return cur;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
