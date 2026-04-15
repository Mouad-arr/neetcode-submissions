class TrieNode{
    constructor(){
        this.children={}
        this.endOfWord=false;
    }
}
class Solution {
    /**
     * @param {character[][]} board
     * @param {string[]} words
     * @return {string[]}
     */
    constructor(){
        this.root = new TrieNode();
    }
    addWord(word){
        let cur=this.root;
        for(const c of word){
            if(!( c in cur.children )){
                cur.children[c]= new TrieNode();
            }
            cur=cur.children[c];
        }
        cur.endOfWord=true;
    }
    res=new Set();
    visit=new Set();
    findWords(board, words) {
        for(const word of words) this.addWord(word);
        const ROWS=board.length  , COLS =board[0].length;
        const dfs = (r,c,node,word) => {
            if( c<0 || r<0 || r>= ROWS || c>=COLS || this.visit.has(`${r},${c}`) || !(board[r][c] in node.children))
                return ;
            node=node.children[board[r][c]];
            word += board[r][c];
            this.visit.add(`${r},${c}`);
            if(node.endOfWord) this.res.add(word);
            dfs(r-1,c,node,word);
            dfs(r+1,c,node,word);
            dfs(r,c-1,node,word);
            dfs(r,c+1,node,word);
            this.visit.delete(`${r},${c}`);
        }
        for(let i=0;i<ROWS;i++){
            for(let j=0;j<COLS;j++)
              dfs(i,j,this.root,'');
        }
        return Array.from(this.res);
    }
}
