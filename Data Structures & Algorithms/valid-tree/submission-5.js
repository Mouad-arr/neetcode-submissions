class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
    validTree(n, edges) {
        if(edges.length>n-1) return false ;
        let visit = new Set();
        const adj = Array.from({ length: n }, () => []);

        for(let p of edges){
            adj[p[0]].push(p[1]);
            adj[p[1]].push(p[0]);
        }
        function dfs(node,par){
            if(visit.has(node))  return false ;
            visit.add(node);
            for(let nei of adj[node]){
                if(nei==par) continue ;
                if(!dfs(nei,node)) return false ;
            }
            return true ;
        }
        return dfs(0,-1) && visit.size ==n ;
    }
}
