class Solution {
    /**
     * @param {number[]} matchsticks
     * @return {boolean}
     */
    makesquare(matchsticks) {
        let n=matchsticks.length;
        let s=matchsticks.reduce((acc,val)=>acc+val,0);
        if(n<=3 || s%4!=0)
           return false;
        matchsticks.sort((a, b) => b - a);
        let length=s/4;
        let sides=[0,0,0,0];
        let dfs= i=>{
            if(i==n)
              return true;
            for(let side=0;side<4;side++){
                if(sides[side]+matchsticks[i]<=length){
                    sides[side]+=matchsticks[i];
                    if(dfs(i+1))
                       return true;
                    sides[side]-=matchsticks[i];
                }
                if(sides[side]==0)
                   break;
            }
            return false;
        }
        return dfs(0);
    }
}
