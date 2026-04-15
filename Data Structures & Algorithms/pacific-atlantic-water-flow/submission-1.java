class Pair {
    int r;
    int c;

    Pair(int r, int c) {
        this.r = r;
        this.c = c;
    }
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pair pair = (Pair) o;
        return r == pair.r && c == pair.c;
    }

    @Override
    public int hashCode() {
        return Objects.hash(r, c);
    }
}
class Solution {
    public int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    
    public void dfs(int r, int c, Set<Pair> visited , int rows,int cols,int[][] heights){
        Pair p = new Pair(r, c);
        if (visited.contains(p)) return;
        visited.add(p);
        for(int[] dir : directions){
            int i = r+dir[0] ;
            int j = c+dir[1] ;
            if(i>=0 && i<rows && j>=0 && j<cols && heights[i][j]>= heights[r][c] ){
                dfs(i,j,visited,rows,cols,heights);
            }
        }

    }
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        Set<Pair> pacific = new HashSet<>();
        Set<Pair> atlantic = new HashSet<>();
        int rows = heights.length ;
        int cols = heights[0].length ;

        for(int i=0 ; i<rows ;i++){
            dfs(i,0,pacific,rows,cols,heights);
            dfs(i,cols-1,atlantic,rows,cols,heights);
        }
        for(int j=0;j<cols;j++){
            dfs(0,j,pacific,rows,cols,heights);
            dfs(rows-1,j,atlantic,rows,cols,heights);
        }
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0 ;i<rows ;i++)
           for(int j=0;j<cols;j++)
             if(pacific.contains(new Pair(i,j)) && atlantic.contains(new Pair(i,j)))
                res.add(Arrays.asList(i, j));
        return res;

    }
}
