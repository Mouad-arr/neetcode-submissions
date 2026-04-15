class Solution {
    Set<List<Integer>> set = new HashSet<>();
    void dfs(int i ,List<Integer> current,int n, int[] nums){
        List<Integer> copy = new ArrayList<>(current);
        Collections.sort(copy);
        if(i==n){
            set.add(copy);
            return ;
        }
        set.add(copy);
        current.add(nums[i]);
        dfs(i+1,current,n,nums);
        current.remove(current.size()-1);
        dfs(i+1,current,n,nums);
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        dfs(0,new ArrayList<>(),nums.length,nums);
        return new ArrayList<List<Integer>>(set);
    }
}
