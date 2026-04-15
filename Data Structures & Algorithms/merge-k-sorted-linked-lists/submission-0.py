# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not lists[0] :
            return 
        N=ListNode()
        cur=N  
        while lists != [[None]*len(lists)]:
            min_index = -1
            min_val = float('inf') 
            for i in range(len(lists)) : 
                if lists[i] and  lists[i].val < min_val :
                    min_val=lists[i].val
                    min_index=i
            if min_index==-1 :
                break
            cur.next=lists[min_index]
            cur=cur.next
            lists[min_index] = lists[min_index].next
        return  N.next