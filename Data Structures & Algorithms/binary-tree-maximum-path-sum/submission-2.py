# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = root.val


        def helper(node):
            nonlocal maxSum
            if not node:
                return 0
            
            leftSum = helper(node.left)
            rightSum = helper(node.right)
            maxSum = max(maxSum, node.val + rightSum + leftSum, node.val + leftSum, node.val + rightSum, node.val)
            return max(node.val, node.val + rightSum, node.val + leftSum)

        helper(root)
        return maxSum


        