class Solution {
public:
    map<pair<int,int>,int> d;
    int dfs(int i,int cur,vector<int>& nums, int target){
        pair<int,int> key = {i, cur};
        if(d.count(key)) return d[key] ;
            
        else if(i == nums.size()-1){
            if(cur==target)
              return 1;
            else return 0;
        }
        d[key]=dfs(i+1,nums[i+1]+cur,nums,target)+dfs(i+1,cur-nums[i+1],nums,target);
        return d[key] ;
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        return dfs(0,nums[0],nums,target)+dfs(0,-nums[0],nums,target);
    }
};
