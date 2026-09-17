class Solution:
    def maxF(self,fruits,start):
            fruit1,fruit2=-1,-1
            i=start
            n=len(fruits)
            res=0
            while i<n :
                if fruit1==-1:
                    fruit1=fruits[i]
                    res+=1
                elif fruit1==fruits[i]:
                    i+=1
                    res+=1
                    continue
                elif fruit2==-1:
                    fruit2=fruits[i]
                    res+=1
                else:
                    if fruits[i]==fruit2:
                        res+=1
                    else:
                        return res
                i+=1
            return res
    def totalFruit(self, fruits: List[int]) -> int:
        m=0
        n=len(fruits)
        if n<=2 :
            return n
        for i in range(n-1):
            m=max(m,self.maxF(fruits,i))
        return m