class Solution {
    public boolean isPalindrome(String s){
        if(s.length() <= 1) return true ;
        int l = 0;
        int r = s.length()-1;
        while(l<r){
            if(s.charAt(l)!=s.charAt(r))
               return false ;
            l+=1;
            r-=1;
        }
        return true ;
    }
    public String longestPalindrome(String s) {
        int n = s.length();
        if(n<=1) return s;
        int reslen=0;
        String res = "";
        for(int i=0;i<n;i++){
            for(int j=i+1;j<=n;j++){
                if(this.isPalindrome(s.substring(i,j))){
                    if(s.substring(i,j).length()>reslen){
                        reslen=s.substring(i,j).length();
                        res=s.substring(i,j);
                    }
                }
            }        
        }
        return res;
    }
}
