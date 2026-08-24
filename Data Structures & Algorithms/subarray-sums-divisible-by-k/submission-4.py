class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n=len(nums)
        prefS=[0]*n
        prefS[0]=nums[0]
        count = 0
        for i in range(1,n):
            prefS[i]=prefS[i-1]+nums[i]
            if prefS[i]%k==0:
                count+=1
        joker=prefS[0]
        if joker % k ==0:
            count +=1
        i=1
        while i<n :
            j=i
            while j<n :
                if (prefS[j]-joker)%k == 0:
                    count+=1
                j+=1
            joker=prefS[i]
            i+=1
        return count

        