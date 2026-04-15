class Pair{
    private int i;
    private int j;

    public Pair(int i,int j){
        this.i=i;
        this.j=j;
    }

    public int getI(){
        return this.i;
    }
    public int getJ(){
        return this.j;
    }   
    @Override 
    public boolean equals(Object p){
        if(this == p) return true;
        if (p == null || getClass() != p.getClass()) return false;
        Pair pair = (Pair) p;
        return i == pair.i && j == pair.j;
    }
    @Override
    public int hashCode() {
        return Objects.hash(i, j);
    }
}
class Solution {
    private Map<Pair,Integer> d = new HashMap<>();
    public int dfs(int i , int cur , int[] nums , int target){
        if(d.containsKey(new Pair(i,cur)))
            return d.get(new Pair(i,cur));
        if(i==nums.length-1){
            if(cur==target){
                return 1 ;
            }
            else
               return 0;
        }
        d.put(new Pair(i,cur),dfs(i+1,nums[i+1]+cur,nums,target)+dfs(i+1,cur-nums[i+1],nums,target)) ;
        return d.get(new Pair(i,cur));
    }
    public int findTargetSumWays(int[] nums, int target) {
        return dfs(0,nums[0],nums,target)+dfs(0,-nums[0],nums,target);
    }
}
