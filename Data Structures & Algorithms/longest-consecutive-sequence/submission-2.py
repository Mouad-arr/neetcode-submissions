class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        longets=0
        L=[0]
        for i in range(len(nums)-1) :
            if nums[i+1]-nums[i] == 1 :
                longets+=1
            elif nums[i+1] == nums[i]:
                longets+=0
            else :
                L.append(longets+1)
                longets=0
        L.append(longets+1)
        if len(nums) == 0 :
            return 0
        else : 
            return max(L)


