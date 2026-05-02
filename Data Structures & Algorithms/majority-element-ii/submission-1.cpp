class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> res ;
        int n = nums.size();
         set<int> s(nums.begin(), nums.end());
        for(int num:s){
            if(count(nums.begin(),nums.end(),num) > n/3)
                   res.push_back(num);
        }
        return res;
    }
};