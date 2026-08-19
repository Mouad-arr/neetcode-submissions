class Solution:
    def customSortString(self, order: str, s: str) -> str:
        newStr=""
        for c in order :
            if c in s :
                newStr+=c*s.count(c)
        for c in set(s):
            if c not in newStr:
                newStr+=c*s.count(c)
        return newStr