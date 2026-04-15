class Solution {
public:
    vector<vector<int>> memo;
    int dfs(int i, int a , vector<int>& coins){
        if(a==0) return 1;
        if(i >= coins.size()) return 0;
        int res=0;
        if(memo[i][a]!=-1) return memo[i][a];
        if(a >= coins[i]){
            res=dfs(i+1,a,coins);
            res+=dfs(i,a-coins[i],coins);
        }
        memo[i][a]=res;
        return res;
    }
    int change(int amount, vector<int>& coins) {
        sort(coins.begin(),coins.end());
        memo.assign(coins.size()+1, vector<int>(amount+1, -1));
        return dfs(0,amount , coins);
    }
};
