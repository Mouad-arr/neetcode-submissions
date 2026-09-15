class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n=len(customers)
        m=0
        res=0
        for i in range(n):
            if grumpy[i]==0:
                res+=customers[i]
            elif i<minutes:
                m+=customers[i]
        i,cur=minutes,m
        while i < n :
            if grumpy[i]==1:
                cur+=customers[i]
            if grumpy[i-minutes]==1:
                cur-=customers[i-minutes]
            i+=1
            m=max(m,cur)
        return res+m