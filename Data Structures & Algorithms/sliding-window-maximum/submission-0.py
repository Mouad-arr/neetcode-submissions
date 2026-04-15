class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1 :
            return nums
        L=[]
        for i in range(len(nums)-k+1):
            L.append(max(nums[i:k+i]))
        return L