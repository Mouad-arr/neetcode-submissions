class Solution {
    /**
     * @param {character[][]} board
     * @return {void} Do not return anything, modify board in-place instead.
     */
    solve(board) {
        let rows = board.length ;
        let cols = board[0].length ;

        function capture(i,j){
            if(i<0 || j<0 || i>=rows || j>= cols || board[i][j]!='O')
               return ;
            board[i][j]='T';
            capture(i,j+1,board);
            capture(i,j-1,board);
            capture(i+1,j,board);
            capture(i-1,j,board);
        }
        for(let i=0;i<rows;i++){
            capture(i,0);
            capture(i,cols-1);
        }
        for(let j=0;j<cols;j++){
            capture(0,j);
            capture(rows-1,j);
        }
        for(let i=0;i<rows;i++)
            for(let j=0;j<cols;j++){
            if(board[i][j]=='T')
                board[i][j]='O';
            else if (board[i][j]=='O')
                board[i][j]='X';
           }
    }
}
