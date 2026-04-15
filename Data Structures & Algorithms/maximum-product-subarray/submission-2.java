class Solution {
    public int maxProduct(int[] nums) {
        int n=nums.length;
        if(n==1) return nums[0];
        int res=0;
        for(int i=0;i<n;i++){
            int curr=1;
            int j=i;
            while(j<n){
                curr*=nums[j];
                res=Math.max(res,curr);
                j++;
            }
        }
        return res;
    }
}
