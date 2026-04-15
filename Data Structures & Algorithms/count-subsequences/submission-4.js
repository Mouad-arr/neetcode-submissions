class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {number}
     */
    numDistinct(s, t) {
        let m = t.length ;
        let n = s.length ;
        let c=0;
        const cur = [];
        const dfs = (i,j)=>{
            if(i>=n || j>=m ) return ;
            if(s.charAt(i)==t.charAt(j)){
                cur.push(s.charAt(i));
                if(cur.length == m) c++;
                else dfs(i+1,j+1);
                cur.pop();
                dfs(i+1,j);
            }
            else{
                dfs(i+1,j);
            }
        }
        dfs(0,0);
        return c;
    }
}
