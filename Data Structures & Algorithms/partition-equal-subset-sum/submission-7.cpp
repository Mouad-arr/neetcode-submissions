class Solution {
public:
    set<int> visited;
    int dfs(int index,int s,vector<int>& nums,int sum){
        int n=nums.size();
        visited.insert(index);
        if(nums[index]+s==sum/2)
           return sum/2;
        if(nums[index]+s > sum/2){
            visited.erase(index);
            return s;
        }
        int cur=0;
        int i=index+1;
        while(i<n && cur!= sum/2){
            cur=dfs(i,s+nums[index],nums,sum);
            i++;
        }
        if(cur==sum/2)
            return sum/2;
        else{
            visited.erase(index);
            return s;
        }
    }
    bool canPartition(vector<int>& nums) {
        int s=0;
        for(int i:nums){
            s+=i;
        }
        if(s%2!=0) return false;
        int index;
        if(dfs(0,0,nums,s)==s/2){
            for(int i=0;i<nums.size();i++)
                if(visited.find(i)!= visited.end()){
                    index=i;
                    break;
                }
            return dfs(index,0,nums,s)==s/2;
        }
        return false;
    }
};