class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for k in range(len(emails)):
            i=0
            while i < len(emails[k]) :
                if emails[k][i]=='.' :
                    emails[k]=emails[k][:i]+emails[k][i+1:]
                elif emails[k][i]=='@' :
                    break
                elif emails[k][i]=='+':
                    j=i
                    while i<len(emails[k]) and emails[k][i]!='@':
                        i+=1
                    emails[k]=emails[k][:j]+emails[k][i:]
                    break
                i+=1    
        return len(set(emails))