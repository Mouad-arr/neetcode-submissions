class Solution {
public:
    set<pair<int,int>> s ;
    bool dfs(int ligne, int col,int i,vector<vector<char>>& board, string word){
        if(i==word.size()) return true;
        if(ligne<0 || col<0 || ligne >= board.size() || col >= board[0].size() ||
        s.count({ligne,col}) || word[i] != board[ligne][col] ) return false;
        s.insert({ligne,col});
        bool res= (dfs(ligne-1,col,i+1,board,word) || dfs(ligne+1,col,i+1,board,word) ||
        dfs(ligne,col-1,i+1,board,word) || dfs(ligne,col+1,i+1,board,word) );
        s.erase({ligne,col});
        return res;
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0;i<board.size();i++)
            for(int j=0;j<board[0].size();j++)
                if(dfs(i,j,0,board,word)) return true;
        return false;
    }
};
