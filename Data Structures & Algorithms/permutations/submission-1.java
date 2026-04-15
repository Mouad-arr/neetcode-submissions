class Solution {
    public List<List<Integer>> permute(int[] nums) {
        if(nums.length == 1){List<List<Integer>> base = new ArrayList<>();
            base.add(List.of(nums[0]));
            return base;} 
        List<List<Integer>> res = new ArrayList<>();
        List<List<Integer>> permut = permute(Arrays.copyOfRange(nums, 1, nums.length));
        for(List<Integer> p : permut ){
            for(int i=0 ; i <= p.size();i++){
                List<Integer> copy = new ArrayList<>(p);
                copy.add(i,nums[0]);
                res.add(copy);
            }
        }
        return res ;
    }
}
