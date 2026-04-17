class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest=""
        n=min([len(s) for s in strs])
        for i in range(n):
            x=strs[0][i]
            for s in strs :
                if x!=s[i] :
                    return longest
            longest+=x
        return longest