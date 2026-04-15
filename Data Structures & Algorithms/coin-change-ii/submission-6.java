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
    private Map< Pair , Integer> d = new HashMap<>();
    public int dfs(int i,int a,int[] coins){
        if(a==0)
           return 1 ;
        if(i>= coins.length) return 0;
        if(d.containsKey(new Pair(i,a)))
            return d.get(new Pair(i,a));
        int res =0;
        if(a >= coins[i]){
            res=dfs(i+1,a,coins);
            res+=dfs(i,a-coins[i],coins);
        }
        d.put(new Pair(i,a),res);
        return res ;
    }
    public int change(int amount, int[] coins) {
        Arrays.sort(coins);
        return dfs(0,amount,coins);
    }
}
