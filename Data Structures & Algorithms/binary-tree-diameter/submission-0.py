# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # res = max of (left hiehgt + right hieght for a node in the tree)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxlen = 0
        def helper(node):
            nonlocal maxlen

            if not node:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            maxlen = max(maxlen, left + right)
            return 1 + max(left, right)

            
            

        helper(root)
        return maxlen