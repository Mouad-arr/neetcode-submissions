class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n= nums.size();
        if(n==1) return nums[0];
        int res =0 ;
        for(int i=0;i<n;i++){
            int curr=1;
            int j=i;
            while(j<n){
                curr*=nums[j];
                res=max(res,curr);
                j++;
            }
        }
        return res;
    }
};
