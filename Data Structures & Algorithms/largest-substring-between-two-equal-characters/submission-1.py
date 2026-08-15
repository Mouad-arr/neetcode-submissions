class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n=len(s)
        if n == len(set(s)):
            return -1
        i=0
        cout=0
        visited=set()
        while i<n :
            if s.count(s[i])>1 and s[i] not in visited:
                j=i+1
                c=s.count(s[i])
                while j<n and c > 1:
                    if s[i]==s[j]:
                        c-=1
                        if c==1 :
                            break
                    j+=1
                cout = max(cout , j-i-1)
                visited.add(s[i])
            i+=1
        return cout