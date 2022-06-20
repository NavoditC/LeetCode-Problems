# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkValidBST(self,root,min_val,max_val):
        if root==None:
            return True
        if root.val<=min_val or root.val>=max_val:
            return False
        return self.checkValidBST(root.left,min_val,root.val) and self.checkValidBST(root.right,root.val,max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_val = -float('inf')
        max_val = float('inf')
        return self.checkValidBST(root,min_val,max_val)
