# easy, no refence was used
class Solution(object):
    def isSameTree(self, p, q):
       
        def check(p,q):
            if p==None and q ==None:
                return True
            if (p==None and q !=None) or( p!=None and q==None):
                return False            
            if p.val !=q.val:
                return False            
            
            bol=check(p.left,q.left) and check(p.right,q.right)
            return bol
        
        
        return check(p,q)
