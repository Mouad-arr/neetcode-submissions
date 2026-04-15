class Pair{
    private int i;
    private int j;

    public Pair(int i,int j){
        this.i=i;
        this.j=j;
    }

    public int getI(){
        return this.i;
    }
    public int getJ(){
        return this.j;
    }   
    @Override 
    public boolean equals(Object p){
        if(this == p) return true;
        if (p == null || getClass() != p.getClass()) return false;
        Pair pair = (Pair) p;
        return i == pair.i && j == pair.j;
    }
    @Override
    public int hashCode() {
        return Objects.hash(i, j);
    }
}
class Solution {
    public Map<Pair,Integer> d = new HashMap<>();
    public int dfs(String text1,String text2,int i,int j , int n ,int m){
        if(d.containsKey(new Pair(i,j))){
            return d.get(new Pair(i,j));
        }
        int res=0;
        if(i==n || j==m) return 0;
        if(text1.charAt(i) == text2.charAt(j)){
           res= 1+dfs(text1,text2,i+1,j+1,n,m);
           d.put(new Pair(i,j),res);
           return res ;
        }
        res= Math.max(dfs(text1,text2,i+1,j,n,m),dfs(text1,text2,i,j+1,n,m));
        d.put(new Pair(i,j),res);
        return res ;
    }
    public int longestCommonSubsequence(String text1, String text2) {
        return dfs(text1,text2,0,0,text1.length(),text2.length());
    }
}