class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n=len(customers)
        pref=[0]*n
        if customers[0]=='Y':
            pref[0]=1
        else:
            pref[0]=-1
        for i in range(1,n):
            if customers[i]=='Y':
                pref[i]=pref[i-1]+1
            else:
                pref[i]=pref[i-1]-1
        mx=-float('INF')
        res=-1
        for i in range(n):
            if pref[i]>mx and pref[i]>0:
                res=i
                mx=pref[i]
        return res+1