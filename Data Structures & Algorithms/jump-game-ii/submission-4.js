class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    jump(nums) {
        let n = nums.length ;
        const dfs= i=>{
            if(i>=n) return 100000;
            if(i==n-1) return 0;
            let res = 100000;
            for(let j=1;j<=nums[i];j++){
                res=Math.min(res,dfs(i+j)+1);
            }
            return res ;
        }
        return dfs(0);
    }
}
