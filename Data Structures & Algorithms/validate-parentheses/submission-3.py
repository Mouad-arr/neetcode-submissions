class Solution:
    def isValid(self, s: str) -> bool:
        D={
            '{' : '}' ,
            '[' : ']' ,
            '(' : ')'
        }
        stack=[]
        for c in s :
            if stack and c==D[stack[-1]] :
                stack.pop()
            elif c in D:
                stack.append(c)
            else :
                return False
        return len(stack) == 0
