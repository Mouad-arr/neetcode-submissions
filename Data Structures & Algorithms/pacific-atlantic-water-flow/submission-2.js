class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights) {
        let ROWS = heights.length ;
        let COLS = heights[0].length ;
        let pacific =  new Set();
        let atlantic = new Set();
        let directions = [[0,1],[0,-1],[1,0],[-1,0]] ;
        function dfs(r,c,visited){
            visited.add(`${r},${c}`);
            for(let [dx,dy] of directions){
                let i = r+dx ;
                let j = c+dy ;
                if(i>=0 && j>=0 && i<ROWS && j<COLS && !visited.has(`${i},${j}`) && heights[i][j] >= heights[r][c]){
                    dfs(i,j,visited);
                }
            }
        }
        for(let i=0 ; i<ROWS ; i++){
            dfs(i,0,pacific);
            dfs(i,COLS-1,atlantic);
        }
        for(let j=0;j<COLS;j++){
            dfs(0,j,pacific);
            dfs(ROWS-1,j,atlantic);
        }
        let res=[] ;
        for(let i=0 ; i<ROWS ;i++){
            for(let j=0 ;j<COLS ;j++){
                if(pacific.has(`${i},${j}`) && atlantic.has(`${i},${j}`))
                   res.push([i,j]);
            }
        }
        return res;
    }
}
