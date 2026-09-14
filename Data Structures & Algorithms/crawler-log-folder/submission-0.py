class Solution:
    def minOperations(self, logs: List[str]) -> int:
        op=0
        for log in logs :
            if log[0]=='.' and log[1]=='.':
                op=max(0,op-1)
            elif log[0]!='.':
                op+=1
        return op