class Solution {
    /**
     * @param {number[]} coins
     * @param {number} amount
     * @return {number}
     */
    coinChange(coins, amount) {
        const memo = new Map();
        function dfs(amount){
            if(amount === 0) return 0;
            if(memo.has(amount))
               return memo.get(amount);
            let res = 1000000000;
            for(let coin of coins){
                if(amount-coin >=0)
                  res=Math.min(res,1+dfs(amount-coin));
            }
            memo.set(amount,res);
            return res ;
        }
        let minCoins=dfs(amount);
        return minCoins < 1000000000 ? minCoins:-1;
    }
}
