class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        
        def traverse(root):
            nonlocal res
            if root==None:
                return 0
            depthL=traverse(root.left)
            depthR=traverse(root.right)
            depth=1+max(depthL,depthR)
            res=max(res,depthL+depthR)
            
            return depth
            
        
        traverse(root)
        return res
        
        
      
      
        

    
            
