class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        n=len(nums)
        memo=[0]*n
        for i in range(n):
            memo[nums[i]-1]=1
        for i in range(n):
            if memo[i]==0:
                res.append(i+1)
        return res