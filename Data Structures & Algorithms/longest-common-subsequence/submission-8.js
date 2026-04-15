class Solution {
    /**
     * @param {string} text1
     * @param {string} text2
     * @return {number}
     */
    longestCommonSubsequence(text1, text2) {
        const n= text1.length;
        const m= text2.length ;
        const memo = Array.from({ length: n }, () => Array(m).fill(-1));
        function dfs(i,j){
            if(i==n || j==m) return 0;
            if(memo[i][j]!=-1) return memo[i][j];
            if(text1.charAt(i)===text2.charAt(j)){
                let res = 1+dfs(i+1,j+1);
                memo[i][j]=res;
                return res;
            }
            let res= Math.max(dfs(i+1,j),dfs(i,j+1));
            memo[i][j]=res;
            return res;
        }

        return dfs(0,0);
    }
}
