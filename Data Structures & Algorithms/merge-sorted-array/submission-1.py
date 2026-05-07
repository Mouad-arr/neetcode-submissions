class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        while i<n:
            while j<m+i and nums2[i]>=nums1[j] :
                j+=1
            for e in range(m+i,j,-1):
                nums1[e]=nums1[e-1]
            nums1[j]=nums2[i]
            i+=1
            j+=1