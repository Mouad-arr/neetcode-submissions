class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        R=[]
        i=1
        isdone=[]     
        for s in strs :
            if s not in isdone :
                E=[]
                for k in range(strs.count(s)) :
                    E.append(s)
                isdone.append(s)
                for j in range(i,len(strs)) :
                    if  "".join(sorted(s)) == "".join(sorted(strs[j])) and strs[j] not in isdone  :
                        E.append(strs[j])
                        isdone.append(strs[j])
                R.append(E)
                i+=1
        return R

