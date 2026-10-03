# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr=[]
        cur=head 
        while cur:
            arr.append(cur.val)
            cur=cur.next
        m=0
        i,j=0,len(arr)-1
        while i<j:
            m=max(m,arr[i]+arr[j])
            i+=1
            j-=1
        return m