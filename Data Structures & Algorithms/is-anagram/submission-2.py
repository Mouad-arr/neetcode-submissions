class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        T=list(t)
        S=list(s)
        if len(t) != len(s) :
            return False
        else :
            for i in T :
                if i in S :
                    S.remove(i)
                else :
                    return False
            if S==[] :
                return True