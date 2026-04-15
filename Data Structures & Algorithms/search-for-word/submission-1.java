class Solution {
    Set<List<Integer>> s = new HashSet<>();
    boolean dfs(int ligne,int col,int i,char[][] board, String word ){
        if(i == word.length()) return true ;
        if( ligne<0 || col<0 || s.contains(Arrays.asList(ligne,col)) || ligne >= board.length || col >= board[0].length || word.charAt(i) != board[ligne][col] ) return false ;
        s.add(Arrays.asList(ligne,col));
        boolean res = (dfs(ligne-1,col,i+1,board,word) || dfs(ligne+1,col,i+1,board,word)
        || dfs(ligne,col-1,i+1,board,word)
        || dfs(ligne,col+1,i+1,board,word)) ;
        s.remove(Arrays.asList(ligne,col));
        return res;
    }
    public boolean exist(char[][] board, String word) {
        for(int i = 0 ; i< board.length ;i++){
            for(int j=0;j<board[0].length;j++)
                if(dfs(i,j,0,board,word)) return true ;
        }
        return false;
    }
}
