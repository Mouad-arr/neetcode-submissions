class Solution:
    def isSub(self,word1,word2) :
        if len(word1)<len(word2) :
            return False
        i=0
        while i<= len(word1)-len(word2):
            if word1[i]==word2[0] :
                if word1[i:i+len(word2)] == word2  :
                    return True
            i+=1
        return False
    def stringMatching(self, words: List[str]) -> List[str]:
        n=len(words)
        res=[]
        for i in range(n) :
            for j in range(n):
                if i==j:
                    continue
                elif self.isSub(words[j],words[i]) :
                    res.append(words[i])
                    break
        return res