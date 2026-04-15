class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int] :
        res=[]
        while len(res) != len(temperatures) :
            stack=[]
            for i in range(len(res),len(temperatures)) :
                if stack :
                    if stack[0] < temperatures[i] :
                        res.append(len(stack))
                        stack=[]
                        break
                    else:
                        stack.append(temperatures[i])
                else :
                    stack.append(temperatures[i])
            if stack :
                res.append(0)
        return res