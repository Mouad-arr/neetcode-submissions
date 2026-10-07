# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        taille = 0
        cur = head

        while cur:
            taille += 1
            cur = cur.next

        k %= taille

        if k == 0:
            return head

        cur = head
        for _ in range(taille - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None

        
        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = head

        return new_head