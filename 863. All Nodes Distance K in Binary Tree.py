
# From the structure we can find the childs, to find the parents we create a parent dictionary to keep the parents of each node.
# now we do BFS to find all nodes with k distance
# another way: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/discuss/143748/Python-Graph-solution-44-ms
# not needed: https://www.youtube.com/watch?v=zWxuGn2nLB8&ab_channel=RickyCho


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
            
            
            
            
        
            
                
        
            
            
