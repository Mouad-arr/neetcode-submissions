from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1[0]!=str2[0]:
            return ""
        n,m=len(str1),len(str2)
        g=gcd(n,m)
        while g>0 :
            if str1==str1[:g]*(n//g) and str2==str2[:g]*(m//g) :
                return str1[:g]
            else :
                g-=1
                while g>0 and ( m%g!=0 or n%g!=0 ) :
                    g-=1
        return ""