class Solution {
    dfs(i,j,grid){
        if(i<0 || j<0 || i>= grid.length || j>= grid[0].length || grid[i][j] =='0')
            return ;
        grid[i][j]='0';
        this.dfs(i+1,j,grid);
        this.dfs(i-1,j,grid);
        this.dfs(i,j+1,grid);
        this.dfs(i,j-1,grid);
    }
    numIslands(grid) {
        let count =0 ;
        for(let i=0;i<grid.length ; i++){
            for(let j=0 ; j<grid[i].length;j++){
                if(grid[i][j]=='1'){
                    this.dfs(i,j,grid);
                    count++;
                }
            }
        }
        return count;
    }
}
