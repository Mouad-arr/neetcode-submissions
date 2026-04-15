class Solution {
    boolean dfs(int i ,int[] nums){
        if(i==nums.length-1) return true;
        else{
            if(nums[i]==0) return false ;
            else{
                for(int j=1;j<=nums[i];j++){
                    if(i+j< nums.length && dfs(i+j,nums)) return true ;
                }
            }
        }
        return false;
    }
    public boolean canJump(int[] nums) {
        return dfs(0,nums);
    }
}
