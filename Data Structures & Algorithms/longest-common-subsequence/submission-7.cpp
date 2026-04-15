class Solution {
public:
    vector<vector<int>> memo;
    int dfs(const string& text1, const string& text2 , int i ,int j ){
        if(i==text1.size()|| j==text2.size()) return 0 ;
        if(memo[i][j]!=-1) return memo[i][j];
        int res;
        if(text1[i]==text2[j]){
           res= 1+dfs(text1,text2,i+1,j+1);
           memo[i][j]=res;
           return res ;
        }
        res= max(dfs(text1,text2,i+1,j),dfs(text1,text2,i,j+1));
        memo[i][j]=res;
        return res ;
    }
    int longestCommonSubsequence(string text1, string text2) {
        memo.assign(text1.size(), vector<int>(text2.size(), -1));
        return dfs(text1,text2,0,0);
    }
};
