class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder or inorder):
            return None
        root=TreeNode(preorder[0])
        index=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:index+1],inorder[:index])
        root.right=self.buildTree(preorder[index+1:],inorder[index+1:])
        
        return root
            
