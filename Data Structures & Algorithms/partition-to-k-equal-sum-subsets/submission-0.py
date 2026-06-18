class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total_sum=sum(nums)
        if total_sum%k!=0:
            return False
        target=total_sum//k
        nums.sort(reverse=True)
        used=[False]*len(nums)
        def backtrack(i,k,subsetSum):
            if k==0:
                return True
            if subsetSum==target:
                return backtrack(0,k-1,0)
            for j in range(i,len(nums)):
                if not used[j] and subsetSum+nums[j]<=target:
                    used[j]=True
                    if backtrack(j+1,k,subsetSum+nums[j]):
                        return True
                    used[j]=False
                else:
                    continue
            return False
        return backtrack(0,k,0)