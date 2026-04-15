# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        precedent = None 
        actuel = head 
        while actuel is not None :
            prochaine = actuel.next
            actuel.next = precedent
            precedent = actuel
            actuel = prochaine
        return precedent