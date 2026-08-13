class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        goodInt=[]
        i=0
        while i<n-2 :
            if num[i]==num[i+1]:
                if num[i+2]==num[i+1]:
                    goodInt.append(int(num[i]+num[i]+num[i]))
                    i+=2
                i+=1
            i+=1
        if len(goodInt)==0:
            return ""
        res=max(goodInt)
        if res==0 :
           return "000"
        return str(res)
        