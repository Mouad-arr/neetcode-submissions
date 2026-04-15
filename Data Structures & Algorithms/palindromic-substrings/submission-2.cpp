class Solution {
public:
    bool isPalindromic(string s){
        int j = s.size();
        if(j<=1) return true ;
        int i=0;
        j--;
        while(i<j){
            if(s[i]!=s[j])
              return false ;
            i++;
            j--;
        }
        return true ;
    }
    int countSubstrings(string s) {
        int n= s.size();
        int count =0;
        if(n<=1) return n ;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<=n ;j++){
                if(isPalindromic(s.substr(i,j-i)))
                   count++;
            }
        }
        return count ;
    }
};
