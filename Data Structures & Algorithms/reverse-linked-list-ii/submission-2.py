# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        prev=head
        for i in range(left-1):
            prev=cur
            cur=cur.next
        R=head
        for i in range(right):
            if R.next == None and left > 1 :
                prev.next=R
            elif i==right-1 and left >1 :
                prev.next=R
            R=R.next
        for i in range(right-left+1):
            n=cur.next
            cur.next=R
            R=cur
            cur=n
        if left ==1 :
            return R
        else :
            return head
        
