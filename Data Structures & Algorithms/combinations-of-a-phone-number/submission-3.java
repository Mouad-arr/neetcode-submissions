class Solution {
    Map<Character,String> D =new HashMap<>(Map.of(
        '2',"abc",
        '3',"def",
        '4',"ghi",
        '5',"jkl",
        '6',"mno",
        '7',"pqrs",
        '8',"tuv",
        '9',"wxyz"
    ));
    List<String> res = new ArrayList<>();
    StringBuilder cur = new StringBuilder();
    public void dfs(String digits,int i , int k){
        if( k == D.get(digits.charAt(i)).length()  ) return ;
        cur.append(D.get(digits.charAt(i)).charAt(k) );
        if( i == digits.length()-1){
            res.add(cur.toString());
            cur.deleteCharAt(cur.length() - 1);
            dfs(digits,i,k+1);
        }
        else{
            dfs(digits,i+1,0);
            cur.deleteCharAt(cur.length() - 1); 
            dfs(digits,i,k+1);
        }
    }
    public List<String> letterCombinations(String digits) {
        if(digits.length()==0) return new ArrayList();
        dfs(digits,0,0);
        return this.res;
    }
}
