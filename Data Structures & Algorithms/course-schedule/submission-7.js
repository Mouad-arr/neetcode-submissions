class Solution {
    /**
     * @param {number} numCourses
     * @param {number[][]} prerequisites
     * @return {boolean}
     */
    canFinish(numCourses, prerequisites) {
        const dict = new Map();
        let requires=[];
        let visited =[];
        for(let i=0;i<numCourses;i++){
            requires.push(false);
            visited.push(false);
        }
        for(let tab of prerequisites){
            if (!dict.has(tab[0])) {
                dict.set(tab[0], new Set());
            }
            dict.get(tab[0]).add(tab[1]);
        }
        function dfs(key){
            visited[key]=true;
            for(let req of dict.get(key)){
                if(dict.has(req) && !requires[req]){
                    if(visited[req]) return ;
                    else {
                        dfs(req);
                        if(!requires[req]) return;
                    }
                }
                else{
                    requires[req]=true;
                }
            }
            requires[key]=true;
        }
        for(let p of dict.keys())
            dfs(p);
        for(let i=0;i<numCourses;i++){
            if(!requires[i] && visited[i])
                return false;
        }
        return true;
    }
}
