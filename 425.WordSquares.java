class TrieNode{
    TrieNode[] nodes;
    List<String> startwith;
    public TrieNode(){
        nodes = new TrieNode[26];
        startwith = new ArrayList<>();
    }
}
class Trie{
    TrieNode root;
    public Trie(){
        root = new TrieNode();
    }
    public void insert(String word){
        TrieNode node = root;
        for(int i=0; i<word.length(); i++){
            int c = word.charAt(i)-'a';
            if(node.nodes[c]==null){
                node.nodes[c] = new TrieNode();
            }
            node.startwith.add(word);
            node = node.nodes[c];
        }
        node.startwith.add(word);
    }
    public List<String> startsWith(String prefix){
        TrieNode node = root;
        for(int i=0; i<prefix.length(); i++){
            int c = prefix.charAt(i)-'a';
            if(node.nodes[c]==null){
                return null;
            }
            node = node.nodes[c];
        }
        return node.startwith;
    }
}
public class Solution {
    public List<List<String>> wordSquares(String[] words) {
        int n = words.length, m = words[0].length();
        char[][] matrix = new char[m][m];
        List<List<String>> result = new ArrayList<>();
        Trie trie = new Trie();
        for(String word:words){
            trie.insert(word);
        }
        search(result, matrix, words, 0, trie);
        return result;
    }
    private void search(List<List<String>> result, char[][] matrix, String[] words, int idx, Trie trie){
        int m = matrix.length;
        if(idx==m){
            List<String> tmp = new ArrayList<>();
            for(int i=0; i<m; i++){
                tmp.add(new String(matrix[i]));
            }
            result.add(tmp);
            return;
        }
        StringBuilder b = new StringBuilder();
        for(int j = 0; j<idx; j++){
            b.append(matrix[idx][j]);
        }
        String prefix = b.toString();
        List<String> candidates = trie.startsWith(prefix);
        if(candidates==null){
            return;
        }
        for(String tmp:candidates){
            for(int i=idx; i<m; i++){
                matrix[idx][i] = tmp.charAt(i);
                matrix[i][idx] = tmp.charAt(i);
            }
            search(result, matrix, words, idx+1, trie);
        }
    }
}
