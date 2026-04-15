class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1 :
            return nums
        queue=deque()
        L=[]
        for idx , num in enumerate(nums) :
            while queue and queue[-1] < num :
                queue.pop()
            queue.append(num)
            if idx >= k-1 :
                L.append(queue[0])
                if nums[idx-k+1] == queue[0] :
                    queue.popleft()
        return L
