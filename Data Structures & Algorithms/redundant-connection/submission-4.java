class Solution {
    public Set<Integer> visited = new HashSet<>();
    public Map<Integer,Set<Integer>> d = new HashMap<>();
    public boolean dfs(int key,int par){
        visited.add(key) ;
        for(int x : d.get(key)){
            if( x==par ) continue;
            else if(visited.contains(x)) continue ;
            else if(d.get(x).contains(par)){
                visited.remove(key);
                return true;}
            else{
                if(dfs(x,par)){
                    visited.remove(key);
                    return true;
                }
            }
        }
        visited.remove(key);
        return false ;
    }
    public int[] findRedundantConnection(int[][] edges) {
        for(int[] p : edges){
            d.putIfAbsent(p[0],new HashSet<>());
            d.get(p[0]).add(p[1]);
            d.putIfAbsent(p[1],new HashSet<>());
            d.get(p[1]).add(p[0]);
        }
        int n=edges.length ;
        int[] res = new int[2];
        for(int i=n-1;i>=0 ;i--){
            if(dfs(edges[i][1],edges[i][0])){
               res= edges[i];
               break;
            }
        } 
        return res ;
    }
}
