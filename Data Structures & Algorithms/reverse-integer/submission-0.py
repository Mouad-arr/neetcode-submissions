class Solution:
    def reverse(self, x: int) -> int:
        s=str(x)
        res=""
        n=len(s)
        if x>=0 :
            for i in range(n):
                res+=s[n-i-1]
            if  int(res) >= 2**31 :
                return 0
            return int(res)
        else:
            for i in range(n-1):
                res+=s[n-i-1]
            if -int(res) < -2**31 :
                return 0
            return -int(res)