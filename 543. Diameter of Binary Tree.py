# https://www.youtube.com/watch?v=X6HnAM83CX0&ab_channel=RickyCho
# https://www.youtube.com/watch?v=bkxqA8Rfv04&ab_channel=NeetCode
# mine is something between
#dept=1+max(depth left, depth right)
# diag=max(diag, l+r+1)

class Solution(object):
    def diameterOfBinaryTree(self, root):
        res=[0]
        # dfs will return depth
        def dfs(root):
            if root is None:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            res[0]=max(res[0],l+r+1)
            return 1+max(l,r)
        dfs(root)    
        return res[0]-1
      
      
        

    
            
