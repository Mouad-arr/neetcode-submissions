class Solution {
public:
    int singleNumber(vector<int>& nums) {
        for(int x:nums){
            if(count(nums.begin(),nums.end(),x)==1){
                 return x;
            }
        }
    }
};
