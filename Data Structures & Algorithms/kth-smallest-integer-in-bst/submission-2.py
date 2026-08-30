# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we just need to know how many nodes on left/right subtree at each node. 
# stuck: how can i keep track of the amount of nodes per side while also return the node val if i satisfy k?
# in order traversal 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # root.left k
        # cur
        # root.right k - left side + 1 

        # build an array using in order travseal
        cnt = 0
        res = 0


        def inorder(node):
            if not node:
                return
            nonlocal cnt
            nonlocal res
            if node.left:
                inorder(node.left)
            if cnt == k:
                return
            cnt += 1
            res = node.val
            if cnt == k:
                return
            if node.right:
                inorder(node.right)
        inorder(root)
        return res
        

        




        
        