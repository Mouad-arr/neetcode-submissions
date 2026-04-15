class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n=len(digits)
        res=[]
        current=[]
        if n==0:
            return []
        D={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        def dfs(digit,j,k) :
            if k == len(D[digit]) :
                return
            current.append(D[digit][k])
            if j == len(digits)-1 :
                res.append(''.join(current))
                current.pop()
                dfs(digit,j,k+1)
            else:
                dfs(digits[j+1],j+1,0)
                current.pop()
                dfs(digit,j,k+1)
        dfs(digits[0],0,0)
        return res