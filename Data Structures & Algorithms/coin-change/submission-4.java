class Solution {
    public Map<Integer,Integer> memo = new HashMap<>();
    public int dfs(int amount , int[] coins){
        if(amount == 0) return 0;
        if(memo.containsKey(amount))
          return memo.get(amount);
        int res = 1000000000;
        for(int coin : coins){
            if(amount-coin>=0)
              res=Math.min(res,1+dfs(amount-coin,coins));
        }
        memo.put(amount,res);
        return res ;
    }
    public int coinChange(int[] coins, int amount) {
        int minCoins = dfs(amount,coins);
        if( minCoins < 1000000000 )
           return minCoins;
        else 
         return -1;
    }
}
