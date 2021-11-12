class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val>q.val:
            p,q=q,p        
        def check(root):        
            if p.val<=root.val and q.val>=root.val:
                return root
            if  p.val<=root.val and q.val<=root.val:
                return check(root.left)
            return check(root.right)            
        return check(root)
