class Solution {
public:
     vector<int> sides = vector<int>(4);
    bool makesquare(vector<int>& matchsticks) {
        int n=matchsticks.size();
        int s=accumulate(matchsticks.begin(),matchsticks.end(),0);
        if(n<=3 || s%4!=0)
            return false;
        sort(matchsticks.begin(),matchsticks.end(), greater<int>());
        int length=s/4;
        return dfs(0,n,length,matchsticks);
    }
    bool dfs(int i,int n , int length,vector<int>& matchsticks){
        if(i==n)
           return true;
        for(int side=0 ; side<4 ;side++){
            if(sides[side]+matchsticks[i]<=length){
                sides[side]+=matchsticks[i];
                if(dfs(i+1,n,length,matchsticks))
                   return true;
                sides[side]-=matchsticks[i];
            }
            if(sides[side]==0)
                break;
        }
        return false;
    }
};