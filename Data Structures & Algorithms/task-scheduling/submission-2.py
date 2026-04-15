class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0 :
            return len(taks)
        my_dict={}
        for task in tasks :
            if task not in my_dict :
                my_dict[task]=1
            else :
                my_dict[task]+=1
        L=sorted(my_dict.items(),key=lambda x : x[1] , reverse=True)
        i=0
        cycle=0
        count = 0
        queue=deque()
        while i < len(L) :
            if L[i][0] not in queue and my_dict[L[i][0]]>0  :
                queue.append(L[i][0])
                my_dict[L[i][0]]-=1
                count+=1
                cycle+=1
            i+=1
            if  max(my_dict.values())==0:
                break
            if  i==len(L) and count <= n :
                cycle+=n-count+1
                queue=deque()
                count=0
                i=0  
                L=sorted(my_dict.items(),key=lambda x : x[1] , reverse=True)
            if count == n+1 :
                queue=deque()
                count=0
                i=0  
                L=sorted(my_dict.items(),key=lambda x : x[1] , reverse=True)
        return cycle    