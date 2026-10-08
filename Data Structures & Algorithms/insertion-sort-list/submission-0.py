# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = head
        cur = head.next

        while cur :
            if prev.val <= cur.val:
                prev = cur
                cur = cur.next
                continue
            
            parc = dummy
            while parc.next.val <= cur.val:
                parc = parc.next

            prev.next = cur.next
            cur.next = parc.next
            parc.next = cur

            cur = prev.next
        return dummy.next