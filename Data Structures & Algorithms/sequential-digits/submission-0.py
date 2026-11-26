class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        m=len(str(low))
        n=len(str(high))
        res=[]
        for k in range(m,n+1):
            num=""
            for j in range(1,k+1):
                num+=str(j)
            if int(num)>=low and int(num)<=high:
                res.append(num)
            j=k+1
            while j<10 and int(num)<=high:
                num=num[1:]+str(j)
                j+=1
                if int(num)>=low and int(num)<=high:
                    res.append(num) 
        return res