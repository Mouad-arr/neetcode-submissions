class Solution {
public:
    vector<vector<vector<int>>> memo;
    bool dfs(int i,int j , int k,string s1, string s2, string s3){
        if(k==s3.size())
           return i==s1.size() && j==s2.size();
        if(memo[i][j][k]!=-1)
          return memo[i][j][k];
        if(i<s1.size() && s1[i]==s3[k])
           if(dfs(i+1,j,k+1,s1,s2,s3)){
               memo[i][j][k]=1;
               return true;
           }
        if(j<s2.size() && s2[j]==s3[k])
           if(dfs(i,j+1,k+1,s1,s2,s3)){
               memo[i][j][k]=1;
               return true;
           }
        memo[i][j][k]=0;
        return false;
        
    }
    bool isInterleave(string s1, string s2, string s3) {
        memo.assign(  s1.size() + 1,vector<vector<int>>(s2.size() + 1,vector<int>(s3.size() + 1, -1)));
        return dfs(0,0,0,s1,s2,s3);
    }
};
