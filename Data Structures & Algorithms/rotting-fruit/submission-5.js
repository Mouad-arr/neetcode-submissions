class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
        let dq=[];
        let minutes =0 , freshFruit=0;
        let n = grid.length;
        let m = grid[0].length ;
        for(let i=0 ;i<n;i++)
           for(let j=0;j<m;j++){
            if(grid[i][j]==2)
               dq.push([i,j]);
            else if (grid[i][j]==1)
               freshFruit++;
           }
        if(freshFruit===0) return 0 ;
        let directions = [[0,1],[0,-1],[1,0],[-1,0]] ;
        while(dq.length!=0 && freshFruit!=0){
            minutes++;
            let l = dq.length ;
            for(let o =0 ;o<l ;o++){
                let [x,y]= dq.shift();
                for(let p of directions){
                    let i = x+p[0];
                    let j = y +p[1];
                    if(i<0|| j<0 || i>=n||j>=m || grid[i][j]==0 || grid[i][j]==2)
                         continue;
                    grid[i][j]=2;
                    freshFruit--;
                    dq.push([i,j]);
                }
            }
        }
        return freshFruit===0 ? minutes:-1;
    }
}
