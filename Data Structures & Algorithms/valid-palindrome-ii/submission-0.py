class Solution:
    def validPalindrome(self, s: str) -> bool:
        oneDeleted=False
        def isPalide(left,right):
            while left <= right:
                if s[left]!=s[right]:
                    nonlocal oneDeleted
                    if oneDeleted :
                        return False
                    else :
                        oneDeleted=True
                        return isPalide(left+1,right) or isPalide(left,right-1)
                else:
                    left+=1
                    right-=1
            return True
        return isPalide(0,len(s)-1)
