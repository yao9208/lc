/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     List<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if(node==null){
            return null;
        }
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
        return copy(node, map);
    }
    private UndirectedGraphNode copy(UndirectedGraphNode node, HashMap<UndirectedGraphNode, UndirectedGraphNode> map){
        UndirectedGraphNode newnode = new UndirectedGraphNode(node.label);
        map.put(node, newnode);
        List<UndirectedGraphNode> neighbors = node.neighbors;
        for(UndirectedGraphNode nei:neighbors){
            if(map.containsKey(nei)){
                newnode.neighbors.add(map.get(nei));
            }else{
                newnode.neighbors.add(copy(nei, map));
            }
        }
        return newnode;
    }
}
