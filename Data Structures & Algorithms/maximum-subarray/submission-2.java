class Solution {
    public int dfs(int i , boolean flag , int[] nums){
        if(i==nums.length){
           if(flag) return 0;
           return -10000;
        }
        if(flag)
           return Math.max(dfs(i+1,true,nums)+nums[i],0);
        else
           return Math.max(nums[i]+dfs(i+1,true,nums),dfs(i+1,false,nums));
    }
    public int maxSubArray(int[] nums) {
        return dfs(0,false,nums);
    }
}
