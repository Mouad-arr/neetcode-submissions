class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        for op in operations :
            if op=='+':
                newScore=record[-1]+record[-2]
                record.append(newScore)
            elif op == 'D' :
                newScore=record[-1]*2
                record.append(newScore)
            elif op=='C': 
                record.remove(record[-1])
            else :
                record.append(int(op))
        return sum(record)