class Solution {
public:
    set<int> visited ;
    bool dfs(int key,int par,vector<vector<int>>& d){
        visited.insert(key);
        for(int x: d[key]){
            if(x==par) continue;
            else if(visited.find(x)!=visited.end()) continue;
            else if(find(d[x].begin(),d[x].end(),par) != d[x].end()){
                visited.erase(key);
                return true;
            }
            else{
                if(dfs(x,par,d)){
                    visited.erase(key);
                    return true;
                }
            }
        }
        visited.erase(key);
        return false;
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<vector<int>> d(n+1);
        for(const auto& p : edges){
            d[p[0]].push_back(p[1]);
            d[p[1]].push_back(p[0]);
        }
        vector<int> res(2) ;
        for(int i=n-1;i>=0;i--){
            if(dfs(edges[i][1],edges[i][0],d)){
               res= edges[i];
               break;
            }
        }
        return res ;
    }
};
