class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if nums[0] > 0 or nums==[] or ( nums[0]==0 and nums[2]>0 ) :
            return []
        else :
            R=[]
            S=[]
            for i in range(len(nums)) :
                k,j=i+1 ,len(nums)-1
                while k < j :
                    if nums[i]+nums[j]+nums[k] == 0 :
                        if{nums[i],nums[j],nums[k]} not in S :
                            R.append([nums[i],nums[j],nums[k]])
                            S.append({nums[i],nums[j],nums[k]})
                        j-=1
                    elif nums[i]+nums[j]+nums[k] > 0 :
                        j-=1
                    elif nums[i]+nums[j]+nums[k] < 0 :
                        k+=1
            return R