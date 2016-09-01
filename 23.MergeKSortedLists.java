/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists==null || lists.length==0){
            return null;
        }
        ListNode dummy = new ListNode(0);
        ListNode ptr = dummy;
        Queue<ListNode> list = new PriorityQueue<ListNode>(lists.length, new Comparator<ListNode>(){
            public int compare(ListNode o1, ListNode o2){
                return o1.val - o2.val;
            }
        });
        for (int i=0; i<lists.length; i++){
            if (lists[i]!=null){
                list.offer(lists[i]);
            }
        }
        while (list.size()>0){
            ListNode cur = list.poll();
            if (cur.next!=null){
                list.offer(cur.next);
            }
            ptr.next = cur;
            cur.next = null;
            ptr = cur;
        }
        return dummy.next;
    }
}
