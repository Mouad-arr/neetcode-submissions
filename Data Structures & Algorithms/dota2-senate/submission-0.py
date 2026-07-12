class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        Rs,Ds=0,0
        for s in senate :
            if s=='D':
                Ds+=1
            else :
                Rs+=1
        nextR,nextD=0,0
        i=0
        while Ds!=0 and Rs!=0 : 
            if i==len(senate):
                i=0
            if senate[i]=='D':
                if nextD==0 :
                    nextR+=1
                    Rs-=1
                else:
                    nextD-=1
                    senate=senate[:i]+senate[i+1:]
                    i-=1
            else :
                if nextR==0 :
                    nextD+=1
                    Ds-=1
                else:
                    nextR-=1
                    senate=senate[:i]+senate[i+1:]
                    i-=1
            i+=1
        if Ds ==0 :
            return "Radiant"
        elif Rs ==0 :
            return "Dire"