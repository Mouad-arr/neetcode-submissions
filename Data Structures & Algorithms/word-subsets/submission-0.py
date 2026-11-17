class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words2=set(''.join(sorted(word)) for word in words2)
        res=[]
        for word in words1:
            good=True
            for wrd in words2 :
                for c in wrd :
                    if c not in word   or wrd.count(c)>word.count(c):
                        good=False
                        break
                if not good :
                    break
            if good :
                res.append(word)
        return res
                
                
