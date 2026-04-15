class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        def rec(opened,closed) :
            if opened==n and closed==n :
                res.append("".join(stack))
            if opened < n :
                stack.append('(')
                rec(opened+1,closed)
                stack.pop()
            if closed<opened :
                stack.append(')')
                rec(opened,closed+1)
                stack.pop()
        rec(0,0)
        return res
