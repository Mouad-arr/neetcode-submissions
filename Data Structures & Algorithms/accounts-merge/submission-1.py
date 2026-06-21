class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        i=0
        while i< len(accounts)  : 
            curEmails=accounts[i][1:]
            for email in curEmails :
                j=i+1
                while j< len(accounts) :
                    if email in accounts[j][1:] :
                        curEmails += accounts[j][1:] 
                        accounts.pop(j)
                        continue
                    j+=1
            curEmails=list(set(curEmails))
            curEmails.sort()
            curEmails.insert(0,accounts[i][0])
            accounts[i]= curEmails
            i+=1
        return accounts