class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        E=set(nums)
        if len(E)==len(nums) :
            return False
        else : 
            return True
        