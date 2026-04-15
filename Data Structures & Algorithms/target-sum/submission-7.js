class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    findTargetSumWays(nums, target) {
        const n = nums.length;
        const memo = new Map();
        const dfs = (i,cur)=>{
            const key = i + "," + cur;
            if(memo.has(key)) 
                return memo.get(key);
            if(i==n-1)
               return cur===target ? 1 : 0;
            memo.set(key,dfs(i+1,cur+nums[i+1])+dfs(i+1,cur-nums[i+1]));
            return memo.get(key);
        }
        return dfs(0,nums[0])+dfs(0,-nums[0]);
    }
}
