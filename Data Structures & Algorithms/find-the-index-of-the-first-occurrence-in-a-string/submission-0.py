class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m=len(haystack),len(needle)
        i=0
        while i+m <= n :
            if haystack[i:i+m]==needle:
                return i
            i+=1
        return -1