class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    longestPalindrome(s) {
        function isPalindrom(s){
            if(s.length <= 1)
              return true;
            let l=0;
            let r =s.length-1;
            while(l<r){
                if(s[l]!=s[r])
                   return false;
                l+=1;
                r-=1;
            }
            return true;
        }
        let n=s.length ;
        if(n<=1) return s ;
        let reslen=0;
        let res='';
        for(let i=0;i<n;i++){
            for(let j=i+1;j<=n ;j++){
                if(isPalindrom(s.substring(i,j))){
                    let curlen=s.substring(i,j).length;
                    if(curlen>reslen){
                        reslen=curlen;
                        res=s.substring(i,j);
                    }
                }
            }
        }
        return res ;
    }
}
