class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        memo=[0]*(pow(n,2))
        for row in grid :
            for e in row :
                memo[e-1]+=1
        ans=[0,0]
        for i in range(pow(n,2)):
            if memo[i]==2 :
                ans[0]=i+1
            elif memo[i]==0:
                ans[1]=i+1
            if ans[0]!=0 and ans[1]!=0 :
                break
        return ans