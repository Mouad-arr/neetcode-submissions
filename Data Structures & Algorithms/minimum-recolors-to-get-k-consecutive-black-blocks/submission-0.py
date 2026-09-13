class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        whites=0
        for i in range(k):
            if blocks[i]=='W':
                whites+=1
        res=whites
        i,j=0,k
        while j<n :
            if blocks[i]==blocks[j]:
                i+=1
                j+=1
                continue
            if blocks[i]=='W':
                whites-=1
            else:
                whites+=1
            res=min(res,whites)
            i+=1
            j+=1
        return res