class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {
        let n =nums.length ;
        const dfs = (i,flag)=>{
            if(i==n)
              return flag ? 0:-10000;
            return flag ? Math.max(dfs(i+1,true)+nums[i],0) : Math.max(dfs(i+1,false),nums[i]+dfs(i+1,true)) ;
        }
        return dfs(0,false);
    }
}
