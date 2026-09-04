class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        toRemove=set()
        for i in range(len(s)):
            if s[i]=='(':
                stack.append((s[i],i))
            elif s[i]==')':
                if len(stack)==0:
                    toRemove.add(i)
                else :
                    stack.pop()
        for st in stack:
            toRemove.add(st[1])
        res=[s[i] for i in range(len(s)) if i not in toRemove]
        return ''.join(res)
