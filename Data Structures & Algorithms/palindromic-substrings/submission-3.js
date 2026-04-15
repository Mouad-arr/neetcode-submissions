class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    countSubstrings(s) {
        function isPalindromic(s){
            let j = s.length ;
            if(j<=1) return true ;
            let i=0;
            j--;
            while(i<j){
                if(s[i]!=s[j])
                   return false ;
                i++;
                j--;
            }
            return true ;
        }
        let n = s.length;
        if(n<=1) return n ;
        let count = 0 ;
        for(let i=0;i<n;i++)
           for(let j = i+1 ;j<=n;j++)
             if(isPalindromic(s.substring(i,j)))
                 count++;
        return count ;
    }
}
