class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic={
            'b':0,
            'a':0,
            'l':0,
            'o':0,
             'n':0
        }
        for c in text :
            if c in dic :
                dic[c]+=1
        r=min(dic['b'],min(dic['a'],dic['n']))
        x=min(dic['l'],dic['o'])
        return min(r,x//2)