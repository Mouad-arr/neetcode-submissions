class Solution:

    def encode(self, strs: List[str]) -> str:
        ret=[]
        for x in strs :
            l=['0','0','0']
            l[-1]=str(len(x) % 10)
            l[-2]=str((len(x) // 10 )% 10)
            l[-3]=str(len(x) // 100)
            ret+="".join(l)
            ret+=[x]
        return "".join(ret)
    def decode(self, s: str) -> List[str]:
        ret=[]
        i=0
        while i<len(s) :
            l= int(s[i:i+3])
            i+=3
            ret.append(s[i:i+l])
            i+=l
        return ret
