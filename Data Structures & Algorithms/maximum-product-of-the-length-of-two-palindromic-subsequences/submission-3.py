class Solution:
    def maxProduct(self, s: str) -> int:
        mp={}
        n=len(s)
        for i in range(1,2**n):
            b = format(i, f'0{n}b')
            st=""
            for j in range(n):
                if b[j]=='1':
                    st+=s[j]
            if st==st[::-1] :
                mp[b]=len(st)
        mx = 0
        for key in mp:
            for k in mp:
                if int(key,2)&int(k,2)!=0:
                    continue
                mx=max(mx,mp[k]*mp[key])
        return mx