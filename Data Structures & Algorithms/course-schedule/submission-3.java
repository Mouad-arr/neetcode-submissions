class Solution {
    public Map<Integer, Set<Integer>> dict = new HashMap<>();
    public List<Boolean> visited = new ArrayList<>();
    public List<Boolean> requires = new ArrayList<>();
    public void dfs(int key){
        visited.set(key,true) ;
        for(int req : dict.get(key)){
            if(dict.containsKey(req) && !requires.get(req)){
                if(visited.get(req))
                   return;
                else{
                    dfs(req);
                    if(!requires.get(req)) return ;
                }
            }
            else{
                requires.set(req,true);
            }
        }
        requires.set(key,true);
    }
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        for(int i=0;i<numCourses;i++){
            this.visited.add(false);
            this.requires.add(false);
        }
        for(int[] tab : prerequisites ){
            this.dict.putIfAbsent(tab[0],new HashSet<>());
            this.dict.get(tab[0]).add(tab[1]);
        }
        for(int key : dict.keySet()){
            dfs(key);
        }
        for(int i=0;i<numCourses;i++){
            if(!requires.get(i) && visited.get(i))
                return false;
        }
        return true;
    }
}
