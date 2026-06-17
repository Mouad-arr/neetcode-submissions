class Solution {
    int[] sides={0,0,0,0};
    public boolean makesquare(int[] matchsticks) {
        int n=matchsticks.length ;
        int s=Arrays.stream(matchsticks).sum();
        if(n<=3 || s%4!=0)
            return false;
        Arrays.sort(matchsticks);
        int length=s/4;
        return dfs(0,n,length,matchsticks);
    }
    boolean dfs(int i,int n,int length,int[] matchsticks){
        if(i==n)
            return true;
        for(int side=0;side<4;side++){
            if(sides[side] + matchsticks[i]<=length){
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

}