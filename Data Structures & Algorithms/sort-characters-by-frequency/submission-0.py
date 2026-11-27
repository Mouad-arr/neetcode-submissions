class Solution:
    def frequencySort(self, s: str) -> str:
        mp={}
        for c in s:
            if c not in mp:
                mp[c]=1
            else:
                mp[c]+=1
        sorted_mp = dict(sorted(mp.items(), key=lambda x: x[1] , reverse=True))
        st=""
        for c in sorted_mp :
            for i in range(sorted_mp[c]):
                st+=c
        return st