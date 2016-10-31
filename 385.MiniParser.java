/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *     // Constructor initializes an empty nested list.
 *     public NestedInteger();
 *
 *     // Constructor initializes a single integer.
 *     public NestedInteger(int value);
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // Set this NestedInteger to hold a single integer.
 *     public void setInteger(int value);
 *
 *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 *     public void add(NestedInteger ni);
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    public NestedInteger deserialize(String s) {
        Deque<NestedInteger> stack = new LinkedList<>();
        NestedInteger cur = null;
        int l = 0, r = 0, num = 0;
        if(s.length()==0){
            return null;
        }
        if(s.charAt(0)!='['){
            return new NestedInteger(Integer.valueOf(s));
        }
        for(r=0; r<s.length(); r++){
            char c = s.charAt(r);
            if(c=='['){
                if(cur!=null){
                    stack.push(cur);
                }
                cur = new NestedInteger();
                l = r+1;
            }
            if(c==']'){
                if(r>l){
                    cur.add(new NestedInteger(Integer.valueOf(s.substring(l, r))));
                }
                if(!stack.isEmpty()){
                    NestedInteger tmp = stack.pop();
                    tmp.add(cur);
                    cur = tmp;
                }
                l=r+1;
            }else if(c==','){
                if(s.charAt(r-1)!=']'){
                    cur.add(new NestedInteger(Integer.valueOf(s.substring(l,r))));
                }
                l = r+1;
            }
        }
        return cur;
    }
}
