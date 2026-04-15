class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        R=[]
        for i in range(len(nums)-1) :
            for j in range(i+1,len(nums)) :
                if nums[i] + nums[j] == target :
                    R.append(i)
                    R.append(j)
        return R
            