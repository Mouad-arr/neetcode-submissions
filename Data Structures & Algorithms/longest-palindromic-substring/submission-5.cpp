class Solution {
public:
    bool isPalindrome(string s){
        if(s.size()<= 1)
           return true ;
        int l=0;
        int r = s.size()-1;
        while(l<r){
            if(s[l]!=s[r])
              return false;
            l+=1;
            r-=1;
        }
        return true ;
    }
    string longestPalindrome(string s) {
        int n = s.size();
        if(n<= 1)
           return s;
        int reslen =0 ;
        string res= "";
        for(int i=0;i<n;i++){
            for(int j=i+1;j<=n ;j++){
                if(isPalindrome(s.substr(i,j-i))){
                    int cuurlen= s.substr(i,j-i).size();
                    if(cuurlen > reslen){
                        reslen=cuurlen ;
                        res=s.substr(i,j-i);
                    }
                }
            }
        }
        return res ;  
    }
};
