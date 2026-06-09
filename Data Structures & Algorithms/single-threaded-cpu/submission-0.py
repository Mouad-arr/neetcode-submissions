class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n=len(tasks)
        listAtt=[0]
        for i in range(1,n) :
            j=0
            while j<len(listAtt) and tasks[listAtt[j]][0]<=tasks[i][0] :
                j+=1
            listAtt.insert(j,i)
        order=[]
        time=tasks[listAtt[0]][0]
        N=len(listAtt)
        while N>0 :
            m=tasks[listAtt[0]][1]
            index=0
            j=1
            while j<N and tasks[listAtt[j]][0] <= time :
                if tasks[listAtt[j]][1] < m:
                    m=tasks[listAtt[j]][1] 
                    index=j
                j+=1
            order.append(listAtt[index])
            time+=tasks[listAtt[index]][1] 
            listAtt.pop(index)
            N = len(listAtt)
        return order