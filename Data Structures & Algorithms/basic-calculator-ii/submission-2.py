class Solution:
    def calculate(self, s: str) -> int:
        op={'+','-','/','*'}
        stack=[]
        n=len(s)
        i=0
        res=0
        while i<n :
            if s[i] in op:
                if s[i]=='*' or s[i]=='/':
                    oper=s[i]
                    i+=1
                    while i<n and s[i]==' ':
                        i+=1
                    digit = s[i]
                    i+=1
                    while i<n and s[i].isdigit():
                        digit+=s[i]
                        i+=1
                    l=stack.pop()
                    if oper=='*':
                        stack.append(l*int(digit))
                    else:
                        stack.append(l//int(digit))
                else:
                    stack.append(s[i])
                    i+=1
            elif s[i].isdigit():
                digit = s[i]
                i+=1
                while i<n and s[i].isdigit():
                    digit+=s[i]
                    i+=1
                stack.append(int(digit))
            else:
                i+=1
        while len(stack)>0:
            l=stack.pop()
            if len(stack)>0:
                o=stack.pop()
                if o=='+':
                    res+=l
                else :
                    res-=l
            else:
                res+=l
        return res