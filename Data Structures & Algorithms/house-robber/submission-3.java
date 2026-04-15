class Solution {
    public int[] memo ;
    public int dfs(int i , int[] nums){
        if(i>=nums.length)
            return 0 ;
        if(memo[i]!=0)
            return memo[i];
        memo[i]=Math.max(dfs(i+1,nums),nums[i]+dfs(i+2,nums));
        return memo[i];
    }
    public int rob(int[] nums) {
        memo = new int[nums.length];
        return dfs(0,nums);
    }
}
