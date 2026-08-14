class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        mp={}
        for word in words :
            for c in word :
                if c in mp:
                    mp[c]+=1
                else :
                    mp[c]=1
        n=len(words)
        for c in mp:
            if mp[c]%n !=0:
                return False
        return True