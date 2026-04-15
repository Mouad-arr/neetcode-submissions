class Solution {
public:
    unordered_map<int,set<int>> D ;
    void dfs(int key , vector<bool>& visited , vector<int>& res){
        if(visited[key]) return ;
        visited[key]=true;
        for(const int x : D[key] ){
            if(D.count(x) && !visited[x] && find(res.begin(), res.end(), x) == res.end()){
                dfs(x,visited,res);
                if(find(res.begin(), res.end(), x) == res.end()) return ;
            }
            else if(!D.count(x) && find(res.begin(), res.end(), x) == res.end() ) res.push_back(x);
            else if(find(res.begin(), res.end(), x) != res.end()) continue;
            else return ;
        }
        res.push_back(key);
    }
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<bool> visited(numCourses,false);
        vector<int> res;
        for(const auto& p :prerequisites ){
            D[p[0]].insert(p[1]);
        }
        for(auto key : D){
            dfs(key.first,visited,res);
            if(find(res.begin(), res.end(), key.first) == res.end())
               return {};
        }
        for(int i=0;i<numCourses;i++){
            if(find(res.begin(), res.end(), i) == res.end())
                res.push_back(i);
        }
        return res ;
    }
};
