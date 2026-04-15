class Solution {
public:
    bool dfs(int i,vector<int>& nums){
        if(i== nums.size() -1 ) return true ;
        else{
            if(nums[i]==0) return false;
            else{
                for(int j=1 ;j<= nums[i];j++){
                    if(i+j< nums.size() && dfs(i+j,nums)) return true;
                }
            }
        }
        return false;
    }
    bool canJump(vector<int>& nums) {
        return dfs(0,nums);
    }
};
