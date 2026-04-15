class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2) :
            return False
        n=len(s1)
        i=0
        s2_dict={}
        for c in s2[i:i+n] :
            if c not in s2_dict :
                s2_dict[c] = 1
            else :
                s2_dict[c] +=1
        s1_dict={}
        for c in s1 :
            if c not in s1_dict :
                s1_dict[c]=1
            else :
                s1_dict[c]+=1
        def isEqual(dict1,dict2) :
            for key in dict1.keys() :
                if key in dict2 :
                    if dict1[key] != dict2[key] :
                        return False
                elif dict1[key] != 0 :
                    return False
            return True
        while i+n <= len(s2) :
            if isEqual(s1_dict,s2_dict) :
                return True
            s2_dict[s2[i]]-=1
            if i+n >= len(s2) :
                break
            else :
                if s2[i+n] in s2_dict :
                    s2_dict[s2[i+n]]+=1
                else :
                    s2_dict[s2[i+n]]=1
            i+=1
        return False