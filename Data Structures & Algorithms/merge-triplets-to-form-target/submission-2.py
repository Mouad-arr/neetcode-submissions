class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        notIn=set()
        for i in range(len(triplets)):
            for j in range(3):
                if triplets[i][j]>target[j] :
                    notIn.add(i)
                    break
        good={
            1:False,
            2:False,
            3:False
        }
        for i in range(len(triplets)):
            if i in notIn :
                continue
            else :
                for j in range(3):
                    if good[j+1]:
                        continue
                    elif target[j]==triplets[i][j]:
                        good[j+1]=True
        for i,isTrue in good.items():
            if not isTrue:
                return False
        return True