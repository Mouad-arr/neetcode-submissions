class Solution {
    int dfs(int i, int[] nums){
        if(i>=nums.length) return 100000;
        if(i==nums.length-1) return 0;
        int res = 100000000 ;
        for(int  j=1 ; j<= nums[i] ;j++){
            res=Math.min(res,dfs(i+j,nums)+1);
        }
        return res ;
    }
    public int jump(int[] nums) {
        return dfs(0,nums);
    }
}
