class Solution:
    def decode(self,s,i):
        cur=""
        n=len(s)
        while i<n and s[i]!=']' and not s[i].isdigit():
            cur+=s[i]
            i+=1
        if i<n and s[i].isdigit():
            digit=s[i]
            i+=1
            while i<n and s[i].isdigit():
                digit+=s[i]
                i+=1
            digit=int(digit)
            i+=1
            nom,i=self.decode(s,i)
            for j in range(digit):
                cur+=nom
        if i<n and s[i]==']' :
            i+=1
        elif i<n and s[i]!=']':
            nom,i=self.decode(s,i)
            cur+=nom
        return cur,i
    def decodeString(self, s: str) -> str:
        decode=""
        i,n=0,len(s)
        while i <n :
            if s[i].isdigit() :
                digit=s[i]
                i+=1
                while i<n and s[i].isdigit():
                    digit+=s[i]
                    i+=1
                digit=int(digit)
                i+=1
                mot,i=self.decode(s,i)
                res=""
                for j in range(digit):
                    res+=mot
                decode+=res
            else:
                decode+=s[i]
                i+=1
                while i<n and not s[i].isdigit() :
                    decode+=s[i]
                    i+=1
        return decode