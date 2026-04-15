class Solution {
    private int c=0;
    public void dfs(int i,int j , List<Character> cur , String s , String t){
        if(i>=s.length() || j>= t.length()) return ;
        if(s.charAt(i)==t.charAt(j)){
            cur.add(s.charAt(i));
            if(cur.size()==t.length()){
                c+=1;
            }
            else{
                dfs(i+1,j+1,cur,s,t);
            }
            cur.removeLast();
            dfs(i+1,j,cur,s,t);
        }
        else 
           dfs(i+1,j,cur,s,t);
    }
    public int numDistinct(String s, String t) {
        dfs(0,0,new ArrayList<>() , s,t);
        return c ;
    }
}
