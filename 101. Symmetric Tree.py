# easy, no refence was used. same as leetcode 100 concept
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
         
       
        def check(p,q):
            if p==None and q ==None:
                return True
            if (p==None and q !=None) or( p!=None and q==None):
                return False            
            if p.val !=q.val:
                return False            
            
            bol=check(p.left,q.right) and check(p.right,q.left)
            return bol
        
        
        return check(root.left,root.right)
