class Solution {
public:
    int dfs(int i,bool flag , vector<int>& nums){
        if(i==nums.size()){
            if(flag) return 0;
            return -100000;
        }
        if(flag){
            return max(dfs(i+1,true,nums)+nums[i],0);
        }
        return max(dfs(i+1,false,nums),nums[i]+dfs(i+1,true,nums));
    }
    int maxSubArray(vector<int>& nums) {
        return dfs(0,false,nums);
    }
};
