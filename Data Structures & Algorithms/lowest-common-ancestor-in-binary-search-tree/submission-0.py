# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    highest common is always the root

    lowest common ancestor would be the higher predecessor between the two nodes predecssors 

    postorder traversal right? 

    my current intuition
    find p and q's direct parent (record the levels)
    lca is the parent with the higher depth level
    
    '''
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pval, qval = p.val, q.val
        minv, maxv = min(pval,qval), max(pval,qval)

        def dfs(node):
            if node == None:
                return None
            if minv <= node.val <= maxv:
                return node
            elif minv > node.val:
                return dfs(node.right)
            else:
                return dfs(node.left)

            

        return dfs(root)


        