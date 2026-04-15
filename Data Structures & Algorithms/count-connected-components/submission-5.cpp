class Solution {
public:
    set<int> visited ;
    void dfs(int n,vector<vector<int>>& d){
        visited.insert(n);
        for(int i : d[n]){
           if(visited.find(i)==visited.end() && d[i].size()>0)
                dfs(i,d); 
            else 
               visited.insert(i); 
        }
    }
    int countComponents(int n, vector<vector<int>>& edges) {
        vector<vector<int>> d(n) ;
        int c=0;
        for(const auto& p : edges){
            d[p[0]].push_back(p[1]);
            d[p[1]].push_back(p[0]);
        }
        for(int i=0;i<n;i++){
            if(d[i].size()>0){
                if(visited.find(i)==visited.end())
                {
                   dfs(i,d);
                   c++;
                }   
            }
        }
        return c+n-visited.size();
    }
};
