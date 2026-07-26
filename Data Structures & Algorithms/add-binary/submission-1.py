class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=""
        rest=0
        n,m=len(a),len(b)
        i,j=n-1,m-1
        while i>=0 and j>=0 :
            if a[i]=='1' :
                if b[j]=='1' :
                    if rest == 0 :
                        res='0'+res
                        rest=1
                    else :
                        res='1'+res
                else :
                    if rest == 0 :
                        res='1'+res
                    else :
                        res='0'+res
            else:
                if b[j]=='1' :
                    if rest == 0 :
                        res='1'+res
                    else :
                        res='0'+res
                else :
                    if rest == 0 :
                        res='0'+res
                    else :
                        res='1'+res
                        rest=0
            i-=1
            j-=1
        while i>=0 :
            if rest==0 :
                res=a[i]+res
            else :
                if a[i]=='1' :
                    res='0'+res
                else :
                    res='1'+res
                    rest=0
            i-=1
        while j>=0 :
            if rest==0 :
                res=b[j]+res
            else :
                if b[j]=='1' :
                    res='0'+res
                else :
                    res='1'+res
                    rest=0
            j-=1
        if rest == 1:
            res ='1'+res
        return res