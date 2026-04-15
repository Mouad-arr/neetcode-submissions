class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        deque<pair<int, int>> dq;
        vector<vector<int>> directions={{0,1},{0,-1},{1,0},{-1,0}};
        int i , j ,l;
        int freshFruit= 0 , minutes=0 ;

        for(i=0;i<n;i++)
          for(j=0;j<m;j++){
              if(grid[i][j]==2) 
                 dq.push_back({i,j});
            else if(grid[i][j]==1)
               freshFruit++;
          }
        if(freshFruit==0) return 0 ;

        while(!dq.empty() && freshFruit!=0){
            l=dq.size();
            minutes++;
            for(int o=0;o<l;o++){
                auto [x, y] = dq.front();
                dq.pop_front();
                for(auto& p : directions){
                    i=x+p[0];
                    j=y+p[1];
                    if(i<0 || j<0 ||i>=n ||j>=m|| grid[i][j]==0 || grid[i][j]==2) 
                         continue;
                    grid[i][j]=2;
                    freshFruit--;
                    dq.push_back({i,j});
                }
            }
        }
        return freshFruit==0 ? minutes : -1;
    }
};
