# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s1 = []
        s2 = []
        if root==None:
            return []
        s1.append(root)
        while(len(s1)>0):
            node = s1.pop()
            s2.append(node.val)
            if node.left!=None:
                s1.append(node.left)
            if node.right!=None:
                s1.append(node.right)
        return s2[::-1]



        
