class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res=[0,0]
        for i in range(1,len(nums)+1):
            if i not in nums :
                res[1]=i
            elif nums.count(i)>1 :
                res[0]=i
            if res[1]!=0 and res[0]!=0:
                break
        return res