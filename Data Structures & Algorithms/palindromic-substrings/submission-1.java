class Solution {
    public boolean isPalindromic(String s){
        if(s.length()<=1) return true;
        int i=0;
        int j=s.length()-1 ;
        while(i<j){
            if(s.charAt(i)!=s.charAt(j))
              return false ;
            i+=1;
            j-=1;
        }
        return true ;
    }
    public int countSubstrings(String s) {
        int n = s.length();
        if(n<=1) return n ;
        int count = 0;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<=n;j++){
                if(this.isPalindromic(s.substring(i,j)))
                  count++;
            }
        }
        return count ;
    }
}
