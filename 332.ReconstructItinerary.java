public class Solution {

    public List<String> findItinerary(String[][] tickets) {
        Map<String, PriorityQueue<String>> map = new HashMap<>();
        LinkedList<String> result = new LinkedList<>();
        for(String[] ticket:tickets){
            map.putIfAbsent(ticket[0], new PriorityQueue<>());
            map.get(ticket[0]).add(ticket[1]);
        }
        dfs("JFK", map, result);
        return result;
    }
    private void dfs(String start, Map<String, PriorityQueue<String>> map, LinkedList<String> result){
        PriorityQueue<String> next = map.get(start);
        while(next!=null && next.size()!=0){
            dfs(next.poll(), map, result);
        }
        result.addFirst(start);
    }
}
