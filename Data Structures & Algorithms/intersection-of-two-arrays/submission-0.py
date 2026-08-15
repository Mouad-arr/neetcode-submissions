class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        for num in set(nums1):
            if num in nums2:
                res.append(num)
        return res