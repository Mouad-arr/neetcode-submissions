class Solution {
public:
    unordered_map<int, unordered_set<int>> dict;
    vector<bool> visited ;
    vector<bool> requires;
    void dfs(int key){
        visited[key]=true;
        for(int req : dict.at(key)){
            if(dict.find(req)!=dict.end() && !requires.at(req) ){
                if(visited.at(req))
                    return ;
                else{
                    dfs(req);
                    if(!requires.at(req)) return ;
                }
            }
            else{
                requires[req]=true;
            }
        }
        requires[key]=true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        for(int i=0;i<numCourses;i++){
            visited.push_back(false);
            requires.push_back(false);
        }
        for(auto &p:prerequisites){
            dict[p.at(0)].insert(p.at(1));
        }
        for(const auto& d : dict){
            int key = d.first;
            dfs(key);
        }
        for(int i=0;i<numCourses;i++){
            if(!requires.at(i) && visited.at(i))
              return false ;
        }
        return true ;
    }
};
