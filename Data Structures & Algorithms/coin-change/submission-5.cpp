class Solution {
public:
    map<int,int> memo;
    int dfs(vector<int>& coins , int amount){
        if(amount == 0) return 0;
        if(memo.count(amount)) return memo[amount];
        int res = 1000000000;
        for(int coin : coins){
            if(amount-coin>=0)
              res=min(res,1+dfs(coins,amount-coin));
        }
        memo[amount]=res;
        return res;
    }
    int coinChange(vector<int>& coins, int amount) {
        int minCoins = dfs(coins,amount);
        if(minCoins<1000000000)
          return minCoins ;
        else return -1;
    }
};
