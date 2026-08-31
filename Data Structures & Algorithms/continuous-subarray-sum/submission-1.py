class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        if n < 2 :
            return False
        pref=[0]*(n-1)
        curS=nums[0]
        for i in range(1,n):
            curS+=nums[i]
            pref[i-1]=curS
            if curS % k == 0 :
                return True
        joker=nums[0]
        i=0
        while i<n-2 :
            for j in range(i+1,n-1):
                if (pref[j]-joker) % k == 0 :
                    return True
            joker=pref[i]
            i+=1
        return False