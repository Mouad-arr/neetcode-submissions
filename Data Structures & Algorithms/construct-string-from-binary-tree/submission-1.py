# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        result = []
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if visited:
                result.append(")")
                continue

            result.append("(")
            result.append(str(node.val))

            stack.append((node, True))

            if node.right:
                stack.append((node.right, False))

            if node.left:
                stack.append((node.left, False))
            elif node.right:
                result.append("()")

        return "".join(result)[1:-1]
