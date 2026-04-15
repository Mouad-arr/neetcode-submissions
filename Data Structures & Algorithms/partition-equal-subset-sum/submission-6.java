class Solution {
    private Set<Integer> visited = new HashSet<>();
    public int dfs(int index, int s , int[] nums,int sum){
        int n = nums.length;
        visited.add(index);
        if(nums[index]+s == sum/2)
           return sum/2;
        if(nums[index]+s > sum/2){
            visited.remove(index);
            return s;
        }
        int cur=0;
        int i = index+1;
        while(i<n && cur != sum/2){
            cur=dfs(i,s+nums[index],nums,sum);
            i++;
        }
        if(cur==sum/2)
           return sum/2;
        else{
            visited.remove(index);
            return s;
        }
    }
    public boolean canPartition(int[] nums) {
        int s=0;
        for(int i:nums){
            s+=i;
        }
        int index=nums.length-1;
        if(s%2!=0)
           return false;
        if(dfs(0,0,nums,s) == s/2){
            for(int i=0;i<nums.length;i++)
                if(!visited.contains(i)){
                    index=i;
                   break;
                }
            return dfs(index,0,nums,s)==s/2;
        }
        return false;
    }
}
