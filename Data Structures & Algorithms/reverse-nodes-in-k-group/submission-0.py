# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=0
        proch=None
        cour=head
        while cour :
            l+=1
            cour=cour.next
        dimmy=ListNode(0,head)
        groupPrev=dimmy
        while l>=k :
            cur = groupPrev.next  
            nex = cur.next
            for _ in range(k - 1):
                cur.next = nex.next    # 1 pointe vers 3
                nex.next = groupPrev.next # 2 pointe vers 1 (qui est le début actuel)
                groupPrev.next = nex  # Le précédent global pointe vers 2 (nouvelle tête)
                nex = cur.next
            groupPrev = cur
            l-=k
        return dimmy.next