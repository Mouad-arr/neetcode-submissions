class Solution:
    def minOperations(self, s: str) -> int:
        first=0
        for i in range(len(s)):
            if i%2==0 and s[i]!='0':
                first+=1
            elif i%2!=0 and s[i]!='1':
                first+=1
        second=0
        for i in range(len(s)):
            if i%2==0 and s[i]=='0':
                second+=1
            elif i%2!=0 and s[i]=='1':
                second+=1
        return min(first,second)