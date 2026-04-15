class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s) :
            return ""
        if Counter(s) == Counter(t) :
            return s
        target=Counter(t)
        count=0
        min_length,l,start=float('inf'),0,0
        for i,c in enumerate(s):
            if c in target :
                target[c]-=1
                if target[c] >=0 :
                    count+=1
            while count == len(t) :
                if i - l+1 < min_length :
                    min_length= i - l+1
                    start=l
                if s[l] in target :
                    target[s[l]]+=1
                    if target[s[l]] > 0 :
                        count-=1
                l+=1
        if min_length == float('inf') :
            return ""
        return s[start:start+min_length]


