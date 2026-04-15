class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=''
        for digit in digits:
            s+=str(digit)
        n=str(int(s)+1)
        res=[]
        for x in n :
            res.append(int(x))
        return res