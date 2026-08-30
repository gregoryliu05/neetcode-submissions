# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxcurval):
            if node == None:
                return 0

            maxnewval = max(maxcurval, node.val)
            
            leftGood = dfs(node.left, maxnewval)
            rightGood = dfs(node.right, maxnewval)
            if maxcurval > node.val:
                return leftGood + rightGood
            return 1 + leftGood + rightGood
        
        return dfs(root, root.val)

        