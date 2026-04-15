class TrieNode{
    HashMap<Character,TrieNode> children ;
    public boolean endOfWord ;
    public TrieNode(){
        this.children = new HashMap<>();;
        this.endOfWord=false ;

    }
}

class Solution {
    public TrieNode root = new TrieNode();

    public void addWord(String word){
        TrieNode cur = this.root ;
        for(char c :  word.toCharArray()){
            if(!cur.children.containsKey(c)){
                cur.children.put(c,new TrieNode());
            }
            cur=cur.children.get(c);
        }
        cur.endOfWord=true;
    }
    record Pair(int x, int y) {}
    public Set<Pair> visit = new HashSet<>();
    public Set<String> res = new HashSet<>();
    public void dfs(int rows,int cols ,int r , int c , TrieNode nood , String word,char[][] board){
        if( r<0 || c<0 || r>= rows|| c>= cols || visit.contains(new Pair(r,c)) || 
           !nood.children.containsKey(board[r][c])) return ;
        visit.add(new Pair(r,c));
        String newWord = word + board[r][c];
        TrieNode node = nood.children.get(board[r][c]) ;
        if(node.endOfWord) res.add(newWord);

        dfs(rows,cols,r-1,c,node,newWord,board);
        dfs(rows,cols,r+1,c,node,newWord,board);
        dfs(rows,cols,r,c+1,node,newWord,board);
        dfs(rows,cols,r,c-1,node,newWord,board);
        visit.remove(new Pair(r,c));
    }
    public List<String> findWords(char[][] board, String[] words) {
        for(String word:words){
            this.addWord(word);
        }
        int rows = board.length;
        int cols = board[0].length ;
        for(int i=0;i<rows ;i++){
            for(int j=0;j<cols;j++){
                dfs(rows,cols,i,j,this.root,new String(),board);
            }}
        return new ArrayList<>(this.res);
    }
}
