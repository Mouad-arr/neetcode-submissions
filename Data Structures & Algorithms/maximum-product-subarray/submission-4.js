class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxProduct(nums) {
        let n= nums.length;
        if(n===1) return nums[0];
        let res =0;
        for(let i=0;i<n;i++){
        let curr=1;
        let j=i;
        while(j<n){
          curr*=nums[j];
          j++;
          res=Math.max(res,curr);
        }
        }
        return res;
    }
}
