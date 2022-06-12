# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        if root.left==None and root.right==None:
            return [[root.val]]
        q = [root]
        ans = []
        flag=0
        while len(q)>0:
            n = len(q)
            temp = []
            for i in range(n):
                node = q.pop(0)
                if flag%2==0:
                    temp.append(node.val)
                else:
                    temp.insert(0,node.val)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
            ans.append(temp)
            flag = 1-flag
        return ans
                    
