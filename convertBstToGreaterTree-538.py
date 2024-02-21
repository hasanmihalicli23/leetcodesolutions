# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sumOfValues = 0
        
        def traversal(node):
            if not node:
                return
            
            traversal(node.right)
            temp = node.val
            node.val += self.sumOfValues
            self.sumOfValues += temp
            traversal(node.left)
        
        traversal(root)
        return root