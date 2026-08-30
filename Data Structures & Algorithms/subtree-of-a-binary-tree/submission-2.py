# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # keep looking until see the subRoot?
        # then call a helper to do all the subtree logic
        def dfs(node, subTreeNode):
            # if not same return fasle
            if not node and not subTreeNode:
                print("hello")
                return True
            elif not node:
                return False
            elif not subTreeNode:
                return False
            else:
                if node.val == subTreeNode.val:
                    return dfs(node.left, subTreeNode.left) and dfs(node.right, subTreeNode.right)
                return False
        
        def maindfs(node,subTreeNode):
            if not subRoot:
                return True
            if not node:
                return False

            if dfs(node, subTreeNode):
                return True
            
            return maindfs(node.left, subTreeNode) or maindfs(node.right, subTreeNode)        
        return maindfs(root, subRoot)


        