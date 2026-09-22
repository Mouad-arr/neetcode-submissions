class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        if n==0 or n==1:
            return n
        ans=1
        maxDiff=0
        j=1
        curS=[nums[0]]
        while j<n :
            curS.append(nums[j])
            if max(curS)-min(curS)<= limit :
                j+=1
            else:
                while max(curS)-min(curS)> limit  :
                    curS=curS[1:]
                j+=1
            ans=max(ans,len(curS))
        return ans
                
                
