class Solution:
    def minSwaps(self, s: str) -> int:
        n=len(s)
        m=0
        balance=0
        for c in s :
            if c == '[':
                balance+=1
            else :
                balance -=1
            if balance < 0 :
                m+=1
                balance+=2
        return m
        

            
