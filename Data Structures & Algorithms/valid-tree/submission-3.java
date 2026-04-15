class Solution {
    List<List<Integer>> adj = new ArrayList<>();
    Set<Integer> visit = new HashSet<>();
    public boolean dfs(int node,int par){
        if(visit.contains(node)) return false ;
        visit.add(node);
        for(int i : adj.get(node)){
            if(i==par) continue ;
            if(!dfs(i,node)) return false ;
        }
        return true ;
    }
    public boolean validTree(int n, int[][] edges) {
        if(edges.length>n-1) return false ;
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for(int[] p : edges){
            adj.get(p[0]).add(p[1]);
            adj.get(p[1]).add(p[0]);
        }
        return dfs(0,-1) && visit.size()==n;
    }
}
