class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[]
        for num in set(nums):
            if nums.count(num) > n//3 :
                res.append(num)
        return res