class Solution {
    private Map<Integer,Integer> d = new HashMap<>();
    public void dfs(int index , int[] nums){
        if(index < 0) return ;
        int n = nums.length;
        int val = nums[index];
        if( d.containsKey(val)){
            int i = index +1 ;
            while(nums[i] != val){
                if(val < nums[i]){
                    d.put(val,Math.max(d.get(val),d.get(nums[i])+1));
                }
                i++;
            }
        }
        else{
            int count=0;
            for(int i = index +1;i<n;i++){
                if( val < nums[i])
                   count = Math.max(count,d.get(nums[i]));
            }
            d.put(val,count+1);
        }
        dfs(index-1,nums);
    }
    public int lengthOfLIS(int[] nums) {
        dfs(nums.length-1,nums);
        int m =0;
        for(Map.Entry<Integer, Integer> entry : d.entrySet()){
            int x = entry.getValue() ;
            if( m < x )
                m=x;
        }
        return m;
    }
}
