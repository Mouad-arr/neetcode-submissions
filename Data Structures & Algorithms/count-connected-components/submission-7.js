class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        const visited = new Set();
         const d = Array.from({ length: n }, () => []);

        for(let p of edges){
            d[p[1]].push(p[0]);
            d[p[0]].push(p[1]);
        }
        function dfs(key){
            visited.add(key);
            for(let x of d[key]){
                if(d[x].length > 0 && !visited.has(x))
                    dfs(x);
                else
                    visited.add(x);
            }
        }
        let N=0;
        for(let i=0;i<n;i++){
            if(d[i].length>0 && !visited.has(i)){
                dfs(i);
                N+=1;
            }
        }
        return N+n-visited.size;
    }
}
