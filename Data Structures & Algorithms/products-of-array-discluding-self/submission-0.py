class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol=[]
        while len(sol) < len(nums) :
            i=len(sol)
            j=0
            s=1
            while j < len(nums) :
                if j != i :
                    s*=nums[j]
                j+=1
            sol.append(s)
        return sol