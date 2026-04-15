class Solution {
public:
    int dfs(int i , vector<int>& nums,vector<int>& memo){
        if(i>=nums.size())
              return 0 ;
        if(memo[i]!=-1)
              return memo[i];
        memo[i]=max(dfs(i+1,nums,memo),nums[i]+dfs(i+2,nums,memo));
        return memo[i];
    }
    int rob(vector<int>& nums) {
        vector<int> memo(nums.size(),-1);
        return dfs(0,nums,memo);
    }
};
