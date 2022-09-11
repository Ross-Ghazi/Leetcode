class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder,postorder):
            if not inorder or not postorder:
                return None            
            root=TreeNode(postorder[-1])
            index=inorder.index(postorder[-1])
            root.left =helper(inorder[:index],postorder[:index])
            root.right=helper(inorder[index+1:],postorder[index:-1])
            return root
        return helper(inorder,postorder)
