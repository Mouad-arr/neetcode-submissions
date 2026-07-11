class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n=len(s)
        memo={}
        if s[n-1]=='1' :
            return False
        if maxJump == 0 :
            return False
        def jump(i) :
            if i==n-1 :
                return True
            if s[i]!='0' :
                return False
            if i in memo :
                return memo[i]
            for j in range(min(i+maxJump,n-1) ,i+minJump-1,-1):
                if jump(j):
                    memo[i]= True
                    return True
            memo[i] = False
            return False
        for j in range(min(maxJump,n-1) ,minJump-1,-1):
            if jump(j) :
                return True
        return False
    