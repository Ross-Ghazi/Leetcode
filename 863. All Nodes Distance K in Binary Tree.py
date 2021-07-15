# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143748/Python-Graph-solution-44-ms
# https://www.youtube.com/watch?v=zWxuGn2nLB8&ab_channel=RickyCho
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:      
        parent={}
        visited=set()
        res=[]
        def dfs(node):
            if node ==None:
                return
            if node.left !=None:            
                parent[node.left]=node
                dfs(node.left)
            if node.right !=None:
                parent[node.right]=node
                dfs(node.right)
        dfs(root) 
        print(parent)
        def bfs(node,level):

            if node.val in visited or level>k:
                return
            visited.add(node.val)
            if level==k:
                res.append(node.val)                
            if node.left != None:
                    bfs(node.left,level+1)
            if node.right != None:
                    bfs(node.right,level+1)                          
                      
            if node in parent:              
                    bfs(parent[node],level+1)        
                
        bfs(target,0)            
        return res
            
            
            
            
        
            
                
        
            
            
