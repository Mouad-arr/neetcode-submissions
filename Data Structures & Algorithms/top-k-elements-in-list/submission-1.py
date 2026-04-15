class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        R=[]
        while len(R)<k :
            istraited=[]
            i=0
            m=0
            key=0
            while i<len(nums) :
                if nums.count(nums[i])>=m and nums[i] not in istraited :
                    m=nums.count(nums[i])
                    key=nums[i]
                    num1 = [num for num in nums if num != key ]
                    istraited.append(key)
                i+=1
            nums= num1
            R.append(key)
        return R


        