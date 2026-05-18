class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=asteroids.copy()
        while True :
            cestBon=True 
            n=len(res)
            i=0
            while i<n-1 :
                if res[i]>=0 and res[i+1]<=0 :
                    if res[i]==abs(res[i+1]):
                        del res[i]
                        del res[i]
                    elif res[i]>abs(res[i+1]) :
                        del res[i+1]
                    else :
                        del res[i]
                    cestBon=False
                else :
                    i+=1
                n=len(res)
            if cestBon:
                break
            else :
                cestBon=True
        if len(res)>=2 :
            n=len(res)
            if res[n-2]>=0 and res[n-1]<=0 :
                if res[n-2]==abs(res[n-1]):
                        del res[n-2]
                        del res[n-2]
                        n=len(res)
                elif res[n-2]>abs(res[n-1]) :
                    del res[n-1]
                else :
                    del res[n-2]
        return res