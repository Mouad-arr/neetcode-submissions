class Solution {
    public int orangesRotting(int[][] grid) {
        int n = grid.length ;
        int m = grid[0].length ;
        int freshFruit=0 , minutes=0;
        Deque<int[]> dq = new ArrayDeque<>();

        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++){
                if(grid[i][j]==2)
                   dq.offer(new int[]{i,j});
                else if(grid[i][j]==1)
                    freshFruit+=1 ;
            }
        
        if(freshFruit == 0) return 0 ;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while(!dq.isEmpty() && freshFruit!=0){
            int l = dq.size();
            for(int o =0 ; o<l;o++){
                int []p=dq.pollFirst();
                int x = p[0];
                int y = p[1];
                int i,j;
                for(int[] dr : directions){
                    int dx=dr[0];
                    int dy=dr[1];
                    i=x+dx;
                    j=y+dy;
                    if(i<0 || j<0 || i>= n || j>=m || grid[i][j]==0 || grid[i][j]==2)
                       continue;
                    freshFruit-=1;
                    grid[i][j]=2;
                    dq.offer(new int[]{i,j});
                }
            }
            minutes+=1;
        }
        return freshFruit==0 ?  minutes : -1 ;
    }
}
