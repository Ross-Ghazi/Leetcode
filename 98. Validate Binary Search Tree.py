#https://www.youtube.com/watch?v=s6ATEkipzow&ab_channel=NeetCode
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return False
        def dfs(node,min,max):
            if node==None:
                return True
            if node.val<=min:
                return False 
            if node.val>=max:
                return False
            return dfs(node.left,min,node.val) and dfs(node.right,node.val,max)
        
            
            
        
        return dfs(root,-float("INF"),float("INF") )
