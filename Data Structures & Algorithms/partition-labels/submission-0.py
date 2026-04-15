class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res=[]
        count=0
        S=""
        for i in range(len(s)):
            flag=True
            S+=s[i]
            if s[i] in s[i+1:]:
                flag = False
            for x in S :
                if x in s[i+1:]:
                    flag=False
                    continue
            if flag:
                res.append(len(S))
                S=""
        return res