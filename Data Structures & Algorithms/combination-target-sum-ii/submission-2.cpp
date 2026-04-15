class Solution {
public:
   set<vector<int>> res ;
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        res.clear();
        sort(candidates.begin(),candidates.end());
        vector<int> cur;
        generatesSubsets(candidates,target,0,cur,0) ;
        return vector<vector<int>> (res.begin(),res.end());
    }
    void generatesSubsets(vector<int>& candidates, int target, int i , vector<int>& cur , int total){
        if(target == total){
            res.insert(cur);
            return ;
        }
        if(total>target || i == candidates.size()) return ;
        cur.push_back(candidates[i]) ;
        generatesSubsets(candidates,target,i+1,cur,total+candidates[i]) ;
        cur.pop_back();
        generatesSubsets(candidates,target,i+1,cur,total) ;
    }
};
