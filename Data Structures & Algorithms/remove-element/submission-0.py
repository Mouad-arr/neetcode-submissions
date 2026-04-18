class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp=[num for num in nums if num!=val]
        for i in range(len(temp)):
            nums[i]=temp[i]
        return len(temp)