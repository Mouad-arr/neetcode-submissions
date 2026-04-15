class Solution:
    def isHappy(self, n: int) -> bool:
        s=0
        S=set()
        while n!=1 :
            char=str(n)
            s=0
            for i in range(len(char)):
                s+=int(char[i])**2
            n=s
            if n in S :
                break
            else:
                S.add(n)
        if n==1:
            return True
        return False