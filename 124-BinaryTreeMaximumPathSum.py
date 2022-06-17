# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_sum = -float('inf')
    def maxPathSumHelper(self,root):
        if root==None:
            return 0
        root_left_sum = self.maxPathSumHelper(root.left)
        root_right_sum = self.maxPathSumHelper(root.right)
        max_side_sum = max(root.val,root.val+max(root_left_sum,root_right_sum))
        max_top_sum = max(max_side_sum,root_left_sum+root_right_sum+root.val)
        self.max_sum = max(self.max_sum,max_top_sum)
        return max_side_sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        x = self.maxPathSumHelper(root)
        return self.max_sum
