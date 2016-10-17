class TrieNode {
    // Initialize your data structure here.
    TrieNode[] nodes;
    boolean end;
    public TrieNode() {
        nodes = new TrieNode[26];
        end = false;
    }
}

class Trie {
    public TrieNode root;

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
    public boolean match(String word, TrieNode curRoot, int pos){
        if(word.length()==pos){
            return curRoot.end==true;
        }
        TrieNode node = curRoot;
        for(int i=pos; i<word.length(); i++){
            char cur = word.charAt(i);
            if(cur=='.'){
                boolean flag = false;
                for(int j=0; j<26; j++){
                    if(node.nodes[j]!=null){
                        flag = match(word, node.nodes[j], i+1);
                        if(flag){
                            return true;
                        }
                    }
                }
                return false;
            }else{
                int idx = word.charAt(i)-'a';
                if(node.nodes[idx]==null){
                    return false;
                }
                node = node.nodes[idx];
            }
        }
        return node.end==true;
    }
}
public class WordDictionary {
    Trie trie;
    public WordDictionary(){
        trie = new Trie();
    }
    // Adds a word into the data structure.
    public void addWord(String word) {
        trie.insert(word);
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return trie.match(word, trie.root, 0);
    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
