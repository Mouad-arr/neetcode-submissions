from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0]!=str2[0]:
            return ""
        n,m=len(str1),len(str2)
        g=gcd(n,m)
        while g>0 :
            s=str1[:g]
            if s!=str2[:g] :
                g-=1
                while  g>0 and  ( m%g!=0 or n%g!=0 ):
                    g-=1
            else :
                good=True
                i=g
                while i<n :
                    if s==str1[i:i+g] :
                        i=i+g
                    else :
                        good = False
                        break
                if good :
                    i=g
                    while i<m :
                        if s==str2[i:g+i] :
                            i=i+g
                        else :
                            good = False
                            break
                if good :
                    return s
                else :
                    g-=1
                    while g>0 and ( m%g!=0 or n%g!=0 ) :
                        g-=1
        return ""