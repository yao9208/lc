# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        small = deque()
        larger = deque()
        self.traverse(root, False, target, k, small)
        self.traverse(root, True, target, k, larger)
        result = []
        while k>0:
            if len(small)==0 and len(larger)==0:
                break
            if len(small)==0:
                result.append(larger.pop())
            elif len(larger)==0:
                result.append(small.pop())
            elif abs(larger[-1]-target)<abs(small[-1]-target):
                result.append(larger.pop())
            else:
                result.append(small.pop())
            k-=1
        return result

    def traverse(self, root, reverse, target, k, queue):
        if not root:
            return
        if reverse:
            self.traverse(root.right, reverse, target, k, queue)
        else:
            self.traverse(root.left, reverse, target, k, queue)
        if not reverse and root.val>target or reverse and root.val<=target:
            return
        queue.append(root.val)
        if len(queue)>k:
            queue.popleft()
        if reverse:
            self.traverse(root.left, reverse, target, k, queue)
        else:
            self.traverse(root.right, reverse, target, k, queue)




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
    public List<Integer> closestKValues(TreeNode root, double target, int k) {
        List<Integer> result = new ArrayList<>();
        Deque<TreeNode> predeStack = new LinkedList<>();
        Deque<TreeNode> succStack = new LinkedList<>();
        initialPredeStack(predeStack, target, root);
        initialSuccStack(succStack, target, root);
        if(!predeStack.isEmpty() && !succStack.isEmpty() && predeStack.peek()==succStack.peek()){
            getSuccessor(succStack);
        }
        while(k-->0){
            if(predeStack.isEmpty()){
                result.add(getSuccessor(succStack));
            }else if(succStack.isEmpty()){
                result.add(getPredecessor(predeStack));
            }else{
                double pre = Math.abs(predeStack.peek().val-target);
                double succ = Math.abs(succStack.peek().val-target);
                if(pre<succ){
                    result.add(getPredecessor(predeStack));
                }else{
                    result.add(getSuccessor(succStack));
                }
            }
        }
        return result;
    }
    private int getPredecessor(Deque<TreeNode> stack) {
        TreeNode cur = stack.pop();
        int ret = cur.val;
        TreeNode p = cur.left;
        while(p!=null){
            stack.push(p);
            p = p.right;
        }
        return ret;
    }
    private int getSuccessor(Deque<TreeNode> stack) {
        TreeNode cur = stack.pop();
        int ret = cur.val;
        TreeNode p = cur.right;
        while(p!=null){
            stack.push(p);
            p = p.left;
        }
        return ret;
    }
    private void initialPredeStack(Deque<TreeNode> stack, double target, TreeNode root){
        TreeNode p = root;
        while(p!=null){
            if(p.val==target){
                stack.push(p);
                return;
            }
            else if(p.val<target){
                stack.push(p);
                p = p.right;
            }else{
                p = p.left;
            }
        }
    }
    private void initialSuccStack(Deque<TreeNode> stack, double target, TreeNode root) {
        TreeNode p = root;
        while(p!=null){
            if(p.val==target){
                stack.push(p);
                return;
            }
            else if(p.val > target) {
                stack.push(p);
                p = p.left;
            }else{
                p = p.right;
            }
        }
    }
}
