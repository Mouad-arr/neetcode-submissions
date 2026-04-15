class Solution {
    public boolean contains(int[] arr,int x){
        for(int i=0;i<index;i++){
            if(arr[i]==x)
               return true;
        }
        return false;
    }
    public Map<Integer,Set<Integer>> D = new HashMap<>();
    public int index=0;
    public void dfs(int key , boolean []visited,int []arr){
            if(visited[key]) return ;
            visited[key]=true;
            for(int x : D.get(key)){
                if(D.containsKey(x) && !visited[x] && !contains(arr,x) ){
                    dfs(x,visited,arr);
                    if(!contains(arr,x))
                       return ;
                }
                else if(!D.containsKey(x) && !contains(arr,x)){
                   arr[index]=x;
                   index++;
                }
                else if(contains(arr,x)) continue;
                else  return ;
            }
            arr[index]=key;
            index++;
       }
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        boolean[] visited = new boolean[numCourses];
        int[] arr = new int[numCourses] ;
        for(int i=0 ;i<numCourses ;i++)
            visited[i]=false;
        for(int[] p : prerequisites){
            D.putIfAbsent(p[0],new HashSet<>());
            D.get(p[0]).add(p[1]);
        }
        for(int key : D.keySet()){
            dfs(key,visited,arr);
            if(!contains(arr,key))
               return new int[]{};
        }
        for(int i =0 ;i<numCourses;i++)
            if(!contains(arr,i)){
                arr[index]=i;
                index++;
            }
        return arr;
    }
}