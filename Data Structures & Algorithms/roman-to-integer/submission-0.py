class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        number=0
        i=0
        dic={
            'V':5,
            'L':50,
            'D':500,
            'M':1000
        }
        while i<n :
            if s[i]=='I' :
                if i+1 < n and s[i+1]=='V' :
                    number+=4
                    i+=1
                elif i+1 < n and s[i+1]=='X' :
                    number+=9
                    i+=1
                else :
                    number+=1
            elif s[i]=='X' :
                if i+1 < n and s[i+1]=='L' :
                    number+=40
                    i+=1
                elif i+1 < n and s[i+1]=='C' :
                    number+=90
                    i+=1
                else :
                    number+=10
            elif s[i]=='C':
                if i+1 < n and s[i+1]=='D' :
                    number+=400
                    i+=1
                elif i+1 < n and s[i+1]=='M' :
                    number+=900
                    i+=1
                else :
                    number+=100
            else :
                number+=dic[s[i]]
            i+=1
        return number
