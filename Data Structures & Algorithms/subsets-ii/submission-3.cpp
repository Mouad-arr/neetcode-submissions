class Solution {
public:
    set<vector<int>> s ;
    void dfs(int i , vector<int>& current , int n , vector<int>& nums ){
        vector<int> copy = current;
        sort(copy.begin(),copy.end());
        s.insert(copy);
        if(i==n) return ;
        current.push_back(nums[i]);
        dfs(i+1,current,n,nums);
        current.pop_back();
        dfs(i+1,current,n,nums);
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int> v ;
        dfs(0, v ,nums.size(),nums);
        return vector<vector<int>>(s.begin(),s.end());
    }
};
