class TrieNode{
public:
    unordered_map<char , TrieNode*> children ;
    bool endOfWord = false ;
};
class Solution {
public:
    TrieNode* root = new TrieNode();
    void addWord(const string& word){
        TrieNode *cur=root;
        for(char c : word){
            if(!cur->children.count(c)) {
                cur->children[c] = new TrieNode();
            }
            cur=cur->children[c];
        }
        cur->endOfWord = true ;
    }
    unordered_set<string> res ;
    vector<vector<bool>> visit ;
    void dfs(int r , int c , TrieNode* node , string word ,vector<vector<char>>& board ){
        if(r<0 || r>= board.size() || c<0 || c>= board[0].size() || 
        visit[r][c] || !node->children.count(board[r][c])) return ;

        visit[r][c] = true ;
        node=node->children[board[r][c]];
        word+=board[r][c];
        if(node->endOfWord) res.insert(word);
        dfs(r-1,c,node,word,board);
        dfs(r+1,c,node,word,board);
        dfs(r,c-1,node,word,board);
        dfs(r,c+1,node,word,board);
        visit[r][c]=false;
    }
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        for(const string& word : words) addWord(word);
    int ROWS= board.size();
    int COLS = board[0].size();
    visit.assign(ROWS,vector<bool>(COLS,false));
    for(int i=0;i<ROWS;i++){
        for(int j=0;j<COLS;j++){
            dfs(i,j,root,"",board);
        }
    }
    return vector<string> (res.begin(),res.end());
}
};
