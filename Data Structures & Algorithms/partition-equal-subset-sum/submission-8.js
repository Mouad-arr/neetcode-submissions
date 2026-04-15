class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    canPartition(nums) {
        let n=nums.length;
        const visited= new Set();
        let sum=0;
        for(let i of nums){
            sum+=i;
        }
        if(sum%2!=0) return false;
        function dfs(index,s){
            visited.add(index);
            if(nums[index]+s==sum/2)
                return sum/2;
            if(nums[index]+s > sum/2){
                visited.delete(index);
                return s;
            }
            let cur=0;
            let i=index+1;
            while(i<n && cur != sum/2){
                cur=dfs(i,s+nums[index]);
                i++;
            }
            if(cur==sum/2)
              return cur;
            else{
                visited.delete(index);
                return s;
            }
        }
        let index;
        if(dfs(0,0)==sum/2){
            for(let i=0;i<n;i++){
                if(!visited.has(i)){
                    index=i;
                    break;
                }
            }
            return dfs(index,0)==sum/2;
        }
        return false;
    }
}
