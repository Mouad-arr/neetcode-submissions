class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        if n==1:
            return 1
        cout =0
        for c in set(s):
            x = s.count(c)
            if x%2 ==0:
                cout += x
            elif x>2 :
                cout += x-1
        return min(n,cout+1)