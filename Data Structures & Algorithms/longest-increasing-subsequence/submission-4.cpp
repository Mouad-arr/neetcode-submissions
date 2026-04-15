class Solution {
public:
    map<int,int> d ;
    void dfs(int index,vector<int>& nums){
        if(index <0) return ;
        int n= nums.size();
        int val=nums[index];
        if(d.find(val) != d.end()){
            int i = index+1;
            while(val != nums[i]){
                if(val < nums[i])
                   d[val] = max(d[val],d[nums[i]]+1);
                i++;
            }
        }
        else{
            int count =0;
            for(int i=index+1;i<n;i++){
                if(val<nums[i])
                    count = max(count,d[nums[i]]);
            }
            d[val]=count+1;
        }
        dfs(index-1,nums);
    }
    int lengthOfLIS(vector<int>& nums) {
        dfs(nums.size()-1,nums);
        int m=0;
        for (auto &[key, value] : d) {
            if(value > m)
               m=value ;
        }
        return m;
    }
};
