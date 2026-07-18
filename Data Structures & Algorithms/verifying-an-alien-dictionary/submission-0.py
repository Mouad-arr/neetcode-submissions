class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count=0
        orders={}
        for c in order :
            orders[c]=count
            count+=1
        n=len(words)
        def compare(s1,s2):
            n1,n2=len(s1),len(s2)
            i,j=0,0
            while i<n1 and j<n2 :
                if s1[i]==s2[j]:
                    i+=1
                    j+=1
                else :
                    return orders[s1[i]] < orders[s2[j]]
            return i==n1

        for i in range(n-1):
            if not compare(words[i],words[i+1]):
                return False
        return True