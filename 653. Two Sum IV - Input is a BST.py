class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        com=set()
        def dfs(node):
            if node==None:
                return False
            if node.val in com:
                return True
            else:
                com.add(k-node.val)               
            return dfs(node.left) or  dfs(node.right)

        return dfs(root)
