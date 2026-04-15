class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    lengthOfLIS(nums) {
        let n = nums.length;
        const d = new Map();
        function dfs(index){
            if(index < 0)
              return ;
            let val = nums[index];
            if(d.has(val)){
                let i = index+1;
                while(val !== nums[i]){
                    if(val < nums[i])
                      d.set(val, Math.max(d.get(val),d.get(nums[i])+1));
                    i++;
                }
            }
            else{
                let count =0;
                for(let i=index+1;i<n;i++){
                    if(val < nums[i])
                      count = Math.max(count, d.get(nums[i]));
                }
                d.set(val,count+1);
            }
            dfs(index-1);
        }
        dfs(n-1);
        let m=0;
        for(let key of d.keys()){
            if(m<d.get(key))
              m=d.get(key);
        }
        return m;
    }
}
