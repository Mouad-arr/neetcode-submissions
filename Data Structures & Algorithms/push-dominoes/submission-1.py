class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        i=0
        n=len(dominoes)
        dominoes=list(dominoes)
        while i<n and dominoes[i]=='.':
            i+=1
        if i == n:
            return ''.join(dominoes)
        if dominoes[i]=='L':
            for j in range(i):
                dominoes[j]='L'
        while i<n :
            if dominoes[i]!='.':
                i+=1
                continue
            k=i-1
            j=i+1
            while j<n and dominoes[j]=='.':
                j+=1
            if j==n :
                if dominoes[k]=='R':
                    for y in range(i,n):
                        dominoes[y]='R'
                i=j
            else:
                if (dominoes[k]=='R' and dominoes[j]=='L') :
                    i=j
                    j-=1
                    k+=1
                    while k<j:
                        dominoes[k]='R'
                        dominoes[j]='L'
                        k+=1
                        j-=1
                elif ( dominoes[k] ==  dominoes[j]):
                    X=dominoes[k]
                    i=j
                    j-=1
                    k+=1
                    while k<=j:
                        dominoes[k]=X
                        dominoes[j]=X
                        k+=1
                        j-=1
                else :
                    i=j
        return ''.join(dominoes)