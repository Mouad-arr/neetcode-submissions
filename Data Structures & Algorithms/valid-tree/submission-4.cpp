class Solution {
public:
    set<int> visit ;
    bool dfs(int node , int par , vector<vector<int>>& adj ){
        if(visit.find(node) != visit.end()) return false ;
        visit.insert(node);
        for(int x : adj[node]){
            if(x==par) continue ;
            if(!dfs(x,node,adj)) return false ;
        }
        return true ;
    }
    bool validTree(int n, vector<vector<int>>& edges) {
        if(edges.size()>n-1) return false ;
        vector<vector<int>> adj(n);
        for(const auto& p :edges){
            adj[p[0]].push_back(p[1]);
            adj[p[1]].push_back(p[0]);
        }

        return dfs(0,-1,adj)&&visit.size()==n;
    }
};
