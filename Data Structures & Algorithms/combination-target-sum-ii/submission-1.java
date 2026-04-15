class Solution {
    Set<List<Integer>> s ;
    public void dfs(int i , List<Integer> currentList,int total,int[] candidates, int target ){
            if(total == target){
                this.s.add(new ArrayList<>(currentList)) ;
                return ;
            }
            if(i == candidates.length|| total > target ){
                return ;
            }
            currentList.add(candidates[i]);
            dfs(i+1,currentList,total+candidates[i], candidates,target);
            currentList.remove(currentList.size() - 1);
            dfs(i+1,currentList,total, candidates,target);
    }
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        s= new HashSet<>();
        Arrays.sort(candidates);
        this.dfs(0,new ArrayList<>(),0 , candidates,target) ;
        return new ArrayList<>(s);
    }
}
