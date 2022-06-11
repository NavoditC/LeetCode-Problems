# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kth1Smallest(self, root: Optional[TreeNode], k: int) -> int:
        if root==None:
            return None

        ans = self.kth1Smallest(root.left,self.k)
        if ans!=None:
            return ans
        if self.k==1:
            return root.val
        else:
            self.k-=1
        ans = self.kth1Smallest(root.right,self.k)
        return ans

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        return self.kth1Smallest(root,k)
