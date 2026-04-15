class TrieNode{
    public HashMap<Character,TrieNode> children = new HashMap<>();
    public boolean endOfWord = false ;
}


class WordDictionary {
    public TrieNode root ;

    public WordDictionary(){
        this.root=new TrieNode();
    }
    public void addWord(String word){
        TrieNode cur = root ;
        for(int i=0 ; i<word.length();i++){
            if(!cur.children.containsKey(word.charAt(i))){
                cur.children.put(word.charAt(i),new TrieNode());
            }
            cur=cur.children.get(word.charAt(i)) ;
        }
        cur.endOfWord = true ;
    }
    public boolean dfs(int j , TrieNode root,String word){
        TrieNode cur=root ;
        for(int i = j ;i<word.length();i++){
            if(word.charAt(i) == '.'){
                for(TrieNode child : cur.children.values()){
                    if(dfs(i+1,child,word)) return true;
                }
                return false;
            }
            else{
                if(!cur.children.containsKey(word.charAt(i)))
                    return false;
                cur=cur.children.get(word.charAt(i)) ;
            }
        }
        return cur.endOfWord;
    }
    public boolean search(String word) {
        return dfs(0,this.root,word);
    }
}
