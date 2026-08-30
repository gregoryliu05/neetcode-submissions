# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we just need to know how many nodes on left/right subtree at each node. 
# stuck: how can i keep track of the amount of nodes per side while also return the node val if i satisfy k?
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # root.left k
        # cur
        # root.right k - left side + 1 
        def dfs(node):
            if not node:
                return 0
        
            leftSide = dfs(node.left)
            rightSide = dfs(node.right)
            return 1 + leftSide+ rightSide


        leftSide = dfs(root.left)
        cnt = leftSide + 1 
        if cnt == k:
            return root.val
        elif cnt > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - cnt)
        




        
        