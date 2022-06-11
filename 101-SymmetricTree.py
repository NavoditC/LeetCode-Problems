# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1==None or root2==None:
            return False
        return root1.val == root2.val and self.isMirror(root1.left,root2.right) and self.isMirror(root1.right,root2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)

        
