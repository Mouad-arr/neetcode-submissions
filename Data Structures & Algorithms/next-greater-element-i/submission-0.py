class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp={}
        stack=[]
        for num in nums2 :
            if not stack:
                stack.append(num)
            else :
                while stack and num > stack[-1] :
                    mp[stack[-1]]=num
                    stack.pop()
                stack.append(num)
        for s in stack:
            mp[s]=-1
        res=[]
        for num in nums1 :
            res.append(mp[num])
        return res
