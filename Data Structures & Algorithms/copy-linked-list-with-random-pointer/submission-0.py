"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return
        res=Node(head.val)
        dict={}
        dict[head]=res
        cur=res
        courant=head.next
        while courant :
            cur.next=Node(courant.val)
            cur=cur.next
            dict[courant]=cur
            courant=courant.next
        for key , valeur in dict.items():
            if key.random is None :
                valeur.random=None
            else :
                valeur.random=dict[key.random]
        return res