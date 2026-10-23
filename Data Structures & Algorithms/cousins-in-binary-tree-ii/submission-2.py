# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque

class Solution:
    def replaceValueInTree(self, root):
        if not root:
            return None

        root.val = 0
        q = deque([root])

        while q:
            level = list(q)
            q.clear()

            next_sum = sum(
                child.val
                for node in level
                for child in (node.left, node.right)
                if child
            )

            for node in level:
                sibling_sum = (
                    (node.left.val if node.left else 0)
                    + (node.right.val if node.right else 0)
                )

                if node.left:
                    node.left.val = next_sum - sibling_sum
                    q.append(node.left)

                if node.right:
                    node.right.val = next_sum - sibling_sum
                    q.append(node.right)

        return root