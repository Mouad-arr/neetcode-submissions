class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split()
        n=len(pattern)
        if n!=len(words):
            return False
        dic={}
        for i in range(n):
            if pattern[i] in dic :
                if dic[pattern[i]]!=words[i]:
                    return False
            else :
                if words[i] in dic.values():
                    return False
                dic[pattern[i]]=words[i]
        return True