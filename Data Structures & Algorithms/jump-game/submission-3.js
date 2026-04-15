class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canJump(nums) {
        let n= nums.length ;
         const dfs = (i)=>{
            if(i==n-1) return true ;
            else {
                if(nums[i]==0) return false ;
                else{
                    for(let j=1 ; j<=nums[i];j++){
                        if(i+j< n && dfs(i+j)) return true ;
                    }
                }
            }
            return false
         }
         return dfs(0);
    }
}
