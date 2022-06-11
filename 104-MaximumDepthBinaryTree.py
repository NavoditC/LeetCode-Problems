# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        d1,d2 = 0,0
        if root.left != None:
            d1 = self.maxDepth(root.left)
        if root.right!=None:
            d2 = self.maxDepth(root.right)
        return 1+max(d1,d2)
        
