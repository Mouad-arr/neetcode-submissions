class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        n=len(allowed)
        count=0
        for word in words :
            cur=0
            for c in set(word) :
                if c in allowed :
                    cur+=1
                else :
                    cur =-1
                    break
            if cur != -1:
                count+=1
        return count