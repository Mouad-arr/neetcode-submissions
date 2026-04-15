class Solution {
public:
    void capture(int i , int j , vector<vector<char>>& board){
        if(i<0 || j<0 || i>= board.size() || j>=board[0].size() || board[i][j] != 'O')
             return ;
        board[i][j]='T';
        capture(i+1,j,board);
        capture(i-1,j,board);
        capture(i,j+1,board);
        capture(i,j-1,board);
    }
    void solve(vector<vector<char>>& board) {
        int rows = board.size();
        int cols = board[0].size();

        for(int i=0 ;i<rows;i++){
            capture(i,0,board);
            capture(i,cols-1,board);
        }
        for(int j=0;j<cols;j++){
            capture(0,j,board);
            capture(rows-1,j,board);
        }   
        for(int i=0;i<rows;i++)
           for(int j=0;j<cols;j++){
            if(board[i][j]=='T')
               board[i][j]='O';
            else if(board[i][j]=='O')
                board[i][j]='X';   
        }
    }
};
