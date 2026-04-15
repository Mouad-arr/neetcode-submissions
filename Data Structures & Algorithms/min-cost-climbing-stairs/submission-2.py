class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<3 :
            return min(cost[0],cost[1])
        for i in range(len(cost)-3,-1,-1) :
            cost[i]=cost[i]+min( cost[i+1] ,cost[i+2] )
        return min(cost[0],cost[1])
        # def dfs(start):
        #     i=start
        #     costOutput=0
        #     if i >= len(cost) :
        #         return 0
        #     if i==len(cost)-1 :
        #         return cost[i]
        #     costOutput+=cost[i]
        #     costOutput+=min(dfs(i+1),dfs(i+2))
        #     return costOutput
        # return min(dfs(0),dfs(1))
