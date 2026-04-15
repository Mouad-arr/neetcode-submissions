class Solution {
    Map<Integer,Set<Integer>> D = new HashMap<>();
    Set<Integer> visited = new HashSet<>();
    public void dfs(int n){
        visited.add(n);
        for(int x : D.get(n)){
            if(D.containsKey(x) && !visited.contains(x))
                dfs(x);
            else
                visited.add(x);
        }
    }
    public int countComponents(int n, int[][] edges) {
        int N=0 ;
        for(int[] p : edges){
            D.putIfAbsent(p[0],new HashSet<>());
            D.putIfAbsent(p[1],new HashSet<>());
            D.get(p[0]).add(p[1]);
            D.get(p[1]).add(p[0]);
        }
        for(int key : D.keySet()){
            if(!visited.contains(key)){
                dfs(key);
                N++;
            }
        }
        return N+n-visited.size();
    }
}
