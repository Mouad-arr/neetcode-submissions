class Solution {
public:
    int dfs(int i,vector<int>& nums){
        if(i>= nums.size()) return 100000;
        if(i==nums.size()-1) return 0;
        int res =1000000;
        for(int j=1;j<= nums[i];j++){
            res=min(res,dfs(i+j,nums)+1);
        }
        return res ;
    }
    int jump(vector<int>& nums) {
        return dfs(0,nums);
    }
};
