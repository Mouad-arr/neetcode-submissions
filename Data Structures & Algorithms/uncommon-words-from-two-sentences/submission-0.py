class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        l1=s1.split(" ")
        l2=s2.split(" ")
        L=[]
        for word in set(l1) :
            if word not in set(l2) and l1.count(word)==1 :
                L.append(word)
        for word in set(l2) :
            if word not in set(l1) and l2.count(word)==1 :
                L.append(word)
        return L
