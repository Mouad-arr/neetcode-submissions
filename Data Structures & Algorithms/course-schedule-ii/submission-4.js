class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {number[]}
     */
    findOrder(numCourses, prerequisites) {
        let visited = [] ;
        let res = [] ;
        const d = new Map();
        for(let i=0;i<numCourses;i++)
           visited.push(false);
        
        function dfs(key){
            if(visited[key]) return;
            visited[key]=true ;
            for(let x of d.get(key)){
                if(d.has(x) && !visited[x] && !res.includes(x)){
                    dfs(x);
                    if(!res.includes(x)) return ;
                }
                else if(!d.has(x) && !res.includes(x)) res.push(x);
                else if(res.includes(x)) continue;
                else return ;
            }
            res.push(key);
        }

        for(let p of prerequisites ){
            if(!d.has(p[0]))
              d.set(p[0],new Set());
            d.get(p[0]).add(p[1]);
        }
        for(let key of d.keys()){
            dfs(key);
            if(!res.includes(key))
              return [];
        }

        for(let i=0;i<numCourses;i++){
            if(!res.includes(i))
              res.push(i);
        }
        return res;
    }
}
