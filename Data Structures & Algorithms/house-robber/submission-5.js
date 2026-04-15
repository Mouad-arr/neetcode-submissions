class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    rob(nums) {
        const memo = new Array(nums.length).fill(-1);
        function dfs(i){
            if(i>=nums.length)
               return 0;
            if(memo[i]!=-1)
               return memo[i];
            memo[i]=Math.max(dfs(i+1),nums[i]+dfs(i+2));
            return memo[i];
        }
        return dfs(0);
    }
}
