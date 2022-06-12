# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [[root.val]]
        nodes = [[]]
        temp=[]
        temp.append(root)
        temp.append(' ')

        while len(temp)>1:
            node = temp.pop(0)
            if node == ' ':
                nodes.append([])
                temp.append(' ')
            else:
                nodes[-1].append(node.val)
                if node.left!=None:
                    temp.append(node.left)
                if node.right!=None:
                    temp.append(node.right)

        return nodes
