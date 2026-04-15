class Solution {
    /**
     * @param {number[][]} edges
     * @return {number[]}
     */
    findRedundantConnection(edges) {
        let n = edges.length ;
        const d = Array.from({ length: n+1 }, () => []);
        const visited= new Set();
        for(const p of edges){
            d[p[0]].push(p[1]);
            d[p[1]].push(p[0]);
        }
        function dfs(key,par){
            visited.add(key);
            for(let x of d[key]){
                if( x== par)continue ;
                if(visited.has(x)) continue;
                if(d[x].includes(par) || dfs(x,par)){
                    visited.delete(key);
                    return true;
                }
            }
            visited.delete(key);
            return false;
        }
        for(let i=n-1;i>=0;i--){
            if(dfs(edges[i][1],edges[i][0]))
               return edges[i];
        }
    }
}
