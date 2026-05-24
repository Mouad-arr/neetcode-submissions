# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left,right=1,n
        m=(left+right)//2
        i=guess(m)
        while i!=0 :
            if i==1:
                left=m+1
            else:
                right=m-1
            m=(left+right)//2
            i=guess(m)
        return m