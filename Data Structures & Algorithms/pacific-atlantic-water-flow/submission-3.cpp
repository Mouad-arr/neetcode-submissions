
class Solution {
public:
    void dfs(int r , int c , vector<vector<bool>>& visited , int rows, int cols ,vector<vector<int>>& heights){
        vector<vector<int>> dirs{{1,0},{-1,0},{0,1},{0,-1}};
        visited[r][c]=true ;
        for(auto& d : dirs){
            int i= r+d[0];
            int j = c+d[1];
            if(i>=0 && j>=0 && i<rows && j<cols && !visited[i][j] && heights[i][j]>=heights[r][c])
                  dfs(i,j,visited,rows,cols,heights);
        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        int rows = heights.size();
        int cols = heights[0].size();
        vector<vector<bool>> pacific(rows, vector<bool>(cols, false));
        vector<vector<bool>> atlantic(rows, vector<bool>(cols, false));
        for(int i=0;i<rows;i++){
            dfs(i,0,pacific,rows ,cols,heights);
            dfs(i,cols-1,atlantic,rows,cols,heights);
        }
        for(int j=0;j<cols;j++){
            dfs(0,j,pacific,rows,cols,heights);
            dfs(rows-1,j,atlantic,rows,cols,heights);
        }
        vector<vector<int>> res ;
        for(int i=0;i<rows;i++)
           for(int j=0;j<cols;j++) 
             if(pacific[i][j] && atlantic[i][j])
                res.push_back({i,j});

        return res;
    }
};
