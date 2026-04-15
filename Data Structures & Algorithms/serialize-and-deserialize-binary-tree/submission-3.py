# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root : 
            return ""
        S=""
        queue=deque([root])
        while True:
            node=queue.popleft()
            if not node:
                S+="*"
            else :
                s=str(node.val)
                if len(s) == 1:
                    S+=s
                else:
                    s="$"+str(len(s))+s
                    S+=s
                queue.append(node.left)
                queue.append(node.right)
            if len(queue) == 0:
                return S
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data=="" :
            return None
        root=TreeNode(int(data[0]))
        queue=deque([root])
        i=1
        while i < len(data) :
            node=queue.popleft()
            if data[i] == "$":
                l=int(data[i+1]) 
                i+=2
                match l :
                    case 2 :
                        if data[i] == "-" :
                            nodeleft=TreeNode(-int(data[i+1]))
                            i+=1
                        else :
                            nodeleft=TreeNode(int(data[i]+data[i+1]))
                            i+=1
                    case 3 :
                        if data[i] == "-" :
                            nodeleft=TreeNode(-int(data[i+1]+data[i+2]))
                            i+=2
                        else :
                            nodeleft=TreeNode(int(data[i]+data[i+1]+data[i+2]))
                            i+=2
                    case 4 :
                        if data[i] == "-" :
                            nodeleft=TreeNode(-int(data[i+1]+data[i+2]+data[i+3]))
                            i+=3
                        else :
                            nodeleft=TreeNode(int(data[i]+data[i+1]+data[i+2]+data[i+3]))
                            i+=3
                    case 5 :
                        if data[i] == "-" :
                            nodeleft=TreeNode(-int(data[i+1]+data[i+2]+data[i+3]+data[i+4]))
                            i+=4
                        else :
                            nodeleft=TreeNode(int(data[i]+data[i+1]+data[i+2]+data[i+3]+data[i+4]))
                            i+=4
                    case 6 :
                        if data[i] == "-" :
                            nodeleft=TreeNode(-int(data[i+1]+data[i+2]+data[i+3]+data[i+4]+data[i+5]))
                            i+=5
                node.left=nodeleft
                queue.append(nodeleft)
            elif data[i] == "*" :
                node.left=None
            else :
                nodeleft=TreeNode(int(data[i]))
                node.left=nodeleft
                queue.append(nodeleft)
            if i+1 == len(data) :
                break
            if data[i+1] == "$" :
                l=int(data[i+2]) 
                i+=2
                match l :
                    case 2 :
                        if data[i+1] == "-" :
                            noderight=TreeNode(-int(data[i+2]))
                            i+=1
                        else :
                            noderight=TreeNode(int(data[i+1]+data[i+2]))
                            i+=1
                    case 3 :
                        if data[i+1] == "-" :
                            noderight=TreeNode(-int(data[i+2]+data[i+3]))
                            i+=2
                        else :
                            noderight=TreeNode(int(data[i+1]+data[i+2]+data[i+3]))
                            i+=2
                    case 4 :
                        if data[i] == "-" :
                            noderight=TreeNode(-int(data[i+2]+data[i+3]+data[i+4]))
                            i+=3
                        else :
                            noderight=TreeNode(int(data[i+1]+data[i+2]+data[i+3]+data[i+4]))
                            i+=3
                    case 5 :
                        if data[i] == "-" :
                            noderight=TreeNode(-int(data[i+2]+data[i+3]+data[i+4]+data[i+5]))
                            i+=4
                        else :
                            noderight=TreeNode(int(data[i+1]+data[i+2]+data[i+3]+data[i+4]+data[i+5]))
                            i+=4
                    case 6 :
                        if data[i] == "-" :
                            noderight=TreeNode(-int(data[i+2]+data[i+3]+data[i+4]+data[i+5]+data[i+6]))
                            i+=5
                node.right=noderight
                queue.append(noderight)
            elif data[i+1] == "*" :
                node.right=None
            else :
                noderight=TreeNode(int(data[i+1]))
                node.right=noderight
                queue.append(noderight)
            i+=2
        return root