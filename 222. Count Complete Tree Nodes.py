# we check left and rigth wing
# if they are the same the number of nodes is *2^depth)-1
# if they are not the same we add 1 to anser and count number of right wing and left wing
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        res=0
        def dfs(root):
            nonlocal res
            if root==None:
                return 0
            cur=root
            l,r=0,0
            while cur!=None:
                cur=cur.left
                l+=1
            cur=root
            while cur!=None:
                cur=cur.right
                r+=1
            if r==l:                
                res+=(2**l)-1
            else:
                res+=1
                dfs(root.left)
                dfs(root.right)
                
                
        dfs(root)
        return res
    
        
        
            
