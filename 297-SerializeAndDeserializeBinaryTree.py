# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return 'X#'
        s1 = self.serialize(root.left)
        s2 = self.serialize(root.right)
        return str(root.val)+'#'+s1+s2


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper_deserialize(mylist):
            val = next(mylist)
            if val=='X':
                return None
            node = TreeNode(int(val))
            node.left = helper_deserialize(mylist)
            node.right = helper_deserialize(mylist)
            return node

        mylist = iter(data.split('#'))
        return helper_deserialize(mylist)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
