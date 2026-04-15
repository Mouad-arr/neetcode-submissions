class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        currentSum=0
        current=[]
        index=0
        candidates.sort()
        def dfs(currentSum,current,index) :
            if currentSum == target :
                res.add(tuple(current.copy()))
                return
            if index == len(candidates) or currentSum > target:
                return
            if currentSum < target :
                current.append(candidates[index])
                dfs(currentSum+candidates[index],current,index+1)
                current.pop()    
                dfs(currentSum,current,index+1)
        dfs(currentSum,current,index)
        return [list(elem) for elem in res]
            


