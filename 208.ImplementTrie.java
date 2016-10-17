class TrieNode {
    // Initialize your data structure here.
    TrieNode[] nodes;
    boolean end;
    public TrieNode() {
        nodes = new TrieNode[26];
        end = false;
    }
}

public class Trie {
    private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
        TrieNode node = root;
        for(int i=0; i<word.length(); i++){
            int cur = word.charAt(i)-'a';
            if(node.nodes[cur]==null){
                node.nodes[cur] = new TrieNode();
            }
            node = node.nodes[cur];
        }
        node.end = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode node = root;
        for(int i=0; i<word.length(); i++){
            int cur = word.charAt(i)-'a';
            if(node.nodes[cur]==null){
                return false;
            }
            node = node.nodes[cur];
        }
        return node.end==true;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
        TrieNode node = root;
        for(int i=0; i<prefix.length(); i++){
            int cur = prefix.charAt(i)-'a';
            if(node.nodes[cur]==null){
                return false;
            }
            node = node.nodes[cur];
        }
        return true;
    }
}

// Your Trie object will be instantiated and called as such:
// Trie trie = new Trie();
// trie.insert("somestring");
// trie.search("key");
