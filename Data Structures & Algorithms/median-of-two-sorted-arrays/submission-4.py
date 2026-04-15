class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1)>len(nums2) :
            nums1,nums2=nums2,nums1
        m,n=len(nums1),len(nums2)
        left,right=0,m
        while left<=right:
            i=(left+right)//2
            j=(n+m+1)//2 -i
            minX=float('inf') if i==m else nums1[i]
            minY=float('inf') if j==n else nums2[j]
            maxX=float('-inf') if i == 0 else nums1[i-1]
            maxY=float('-inf') if j==0 else nums2[j-1]
            if minX >= maxY and minY >= maxX :
                if (n+m) % 2 == 1 :
                    return max(maxX,maxY)
                else : 
                    return (max(maxX,maxY)+min(minY,minX))/2
            else :
                if maxX > minY :
                    right= i-  1
                else :
                    left = i + 1