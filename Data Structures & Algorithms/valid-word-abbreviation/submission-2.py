class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n,m=len(word),len(abbr)
        i,j=0,0
        while i<n and j<m:
            if abbr[j].isdigit():
                digit=abbr[j]
                if int(digit)==0:
                    return False
                j+=1
                while j<m and abbr[j].isdigit():
                    digit+=abbr[j]
                    j+=1
                i+=int(digit)
            else :
                if abbr[j]!=word[i]:
                    return False
                i+=1
                j+=1
        return i==n and j==m